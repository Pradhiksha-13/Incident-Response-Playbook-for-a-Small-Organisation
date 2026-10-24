#!/usr/bin/env python3
"""Turn an incident-form submission (JSON) into a DRAFT incident report (Markdown).

- Runs locally; no network calls; no AI API. Safe for fictional/sample data.
- Mirrors what a Make/Zapier flow does: form -> router by type -> text template -> draft doc.
- Output is a DRAFT: a human must review it. It never sends anything externally.
Usage: python 08_incident_to_report.py 08_sample_form.json > draft.md
"""
import json, sys
from datetime import datetime, timedelta

NEXT_STEPS = {
    "lost or stolen laptop": [
        "Remote-lock/locate device; revoke sessions and reset owner's passwords.",
        "Confirm whether disk encryption was on.",
        "Remote-wipe only after Incident Lead approves.",
        "File police report if stolen."],
    "malware alert": [
        "Disconnect from network; leave device on and untouched unless Tech Lead instructs otherwise.",
        "Screenshot alert; do not pay or contact attackers.",
        "Check file server/other machines for spread.",
        "Rebuild from known-good image; restore from clean backup."],
    "account takeover": [
        "Reset password from a clean device; sign out all sessions.",
        "Re-register MFA; remove unknown MFA devices.",
        "Remove malicious inbox rules, forwarding, app consents.",
        "Warn contacts who received suspicious messages."],
}
DEFAULT_STEPS = ["Notify Technical Lead and Incident Lead.", "Preserve evidence; do not delete anything.", "Classify the incident using the playbook."]

SENSITIVE = ("student", "staff", "research", "credentials", "unknown")

def main(path):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    noticed = datetime.fromisoformat(d["time_noticed"])
    deadline = noticed + timedelta(hours=6)
    itype = d.get("incident_type", "other")
    steps = NEXT_STEPS.get(itype.strip().lower(), DEFAULT_STEPS)
    data = d.get("data_involved", "unknown").lower()
    flag = any(s in data for s in SENSITIVE)
    severity = "High" if ("ransom" in d.get("description", "").lower() or "encrypted" in d.get("description", "").lower()) else ("Medium" if flag else "Low")
    inc_id = "ADL-" + noticed.strftime("%Y") + "-DRAFT-" + noticed.strftime("%m%d%H%M")

    out = []
    out.append(f"# DRAFT Incident Report {inc_id}")
    out.append("> **DRAFT generated automatically. A human must review before use. Not sent anywhere.**\n")
    out.append(f"- **Reported by:** {d['reporter_name']} ({d['reporter_role']})")
    out.append(f"- **Time noticed:** {noticed.isoformat()}")
    out.append(f"- **Type:** {itype}")
    out.append(f"- **Suggested severity (rule-based, confirm):** {severity}")
    out.append(f"- **Systems/accounts affected:** {d['systems_affected']}")
    out.append(f"- **Data involved:** {d['data_involved']}\n")
    out.append("## What happened (as reported)")
    out.append(d["description"] + "\n")
    out.append("## Actions already taken")
    out.append(d["actions_taken"] + "\n")
    out.append("## Suggested next steps (from playbook)")
    out += [f"- [ ] {s}" for s in steps]
    out.append("\n## Reporting decision (HUMAN REQUIRED)")
    out.append(f"- If Incident Lead + Institute IT/legal decide this is reportable to CERT-In, the 6-hour window from noticing ends at **{deadline.isoformat()}**.")
    out.append("- Decision by: ________  Time: ________  Reason: ________")
    if flag:
        out.append("- ⚠ Data involved may be sensitive: involve Institute IT/legal officer now.")
    out.append("\n## Review checklist")
    out.append("- [ ] Facts verified  - [ ] Times correct  - [ ] No personal data in the draft  - [ ] Approved by Incident Lead")
    print("\n".join(out))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
