# One-Page Playbooks — Applied Data Lab (fictional)

*Each playbook fits one printed page. Rule 0 for all: **note the time you noticed, tell the Technical Lead, don't delete anything.***

---
## PLAYBOOK 1 — LOST OR STOLEN LAPTOP
**Trigger:** Laptop/phone/USB with lab data missing. **Severity default:** Medium (High if unencrypted or holds student/research-sensitive data).

| Phase | Actions | Owner |
|---|---|---|
| **Detect** | Record: device, owner, last seen, time noticed. Was it encrypted? Passcode set? What data/accounts were on it? | Reporter → Tech Lead |
| **Contain** | 1) Remote-lock/locate via device manager. 2) Reset owner's passwords; revoke sessions/tokens. 3) Remove device from Wi-Fi/VPN/cloud allow-lists. 4) **Remote-wipe only after Incident Lead agrees** (may destroy evidence/recovery chance). 5) If stolen: file police report (cyber/local). | Tech Lead; Incident Lead approves |
| **Decide** | Does it hold personal or sensitive data and was it unencrypted? → Incident Lead + Institute IT/legal decide on **CERT-In/data-protection reporting (6-hour clock from noticing)**. | Incident Lead |
| **Recover** | Issue replacement; restore from backup; re-enrol with encryption. Monitor accounts 14 days. | Tech Lead |
| **Review** | Was encryption on? How long to notice? Update device policy. | All |

**Do not:** assume "it's encrypted" without checking; keep using the same passwords; post publicly about the loss with details.

---
## PLAYBOOK 2 — MALWARE ALERT
**Trigger:** Antivirus/EDR alert, ransom note, popups, unexpected encryption/slowness. **Severity default:** Medium; **High** if ransom note, multiple machines, or server affected.

| Phase | Actions | Owner |
|---|---|---|
| **Detect** | Screenshot alert; note host name, user, time, file/URL involved. Don't click further. Check if other machines show it. | Reporter → Tech Lead |
| **Contain** | 1) **Disconnect from network** (unplug Ethernet / disable Wi-Fi). 2) **Leave device on and untouched** unless files are actively being encrypted and Tech Lead/IT instructs power-off (preserves memory evidence vs. stops damage — human call). 3) Block the file hash/URL via IT. 4) Disable the user's accounts until cleared. 5) Check file-server for spread; take shares offline if needed. | Tech Lead |
| **Decide** | Ransomware, data theft or unauthorised access → treat as **potentially reportable to CERT-In (6 hours)**; escalate to Incident Lead + Institute IT/legal. **Never pay or contact attackers.** | Incident Lead |
| **Recover** | Rebuild from known-good image (not just "clean"); reset all credentials used on the device; restore data from **clean, older** backup; scan before reconnecting. | Tech Lead |
| **Review** | Entry point? (email, USB, download). Patch status? Backup worked? | All |

**Do not:** wipe immediately, run random "cleaner" tools from the internet, plug the device into other machines, pay ransom.

---
## PLAYBOOK 3 — ACCOUNT TAKEOVER
**Trigger:** Unknown logins/locations, password changed unexpectedly, mailbox rules or forwards you didn't set, MFA prompts you didn't request, phishing sent from a lab account. **Severity default:** Medium; High for admin/staff/research-data accounts.

| Phase | Actions | Owner |
|---|---|---|
| **Detect** | Note account, time, what changed, any suspicious email or link clicked. Screenshot sign-in log. | Reporter → Tech Lead |
| **Contain** | 1) From a **clean device**, reset the password and **sign out all sessions**. 2) Re-register MFA (remove unknown devices/methods). 3) Remove malicious inbox rules, forwarding, app consents, API tokens. 4) Reset passwords reused elsewhere. 5) Warn contacts who got suspicious mail from that account. | Tech Lead + account owner |
| **Decide** | Unauthorised access to systems/data or identity/phishing abuse → Incident Lead + Institute IT/legal decide on **CERT-In reporting (6-hour clock)**. | Incident Lead |
| **Recover** | Review audit logs for data accessed/downloaded; restore changed files; monitor 14 days; confirm with user. | Tech Lead |
| **Review** | Was MFA enabled? Password reuse? Phishing click? Update training. | All |

**Do not:** reset from the possibly-infected machine, just "change the password" without killing sessions, ignore forwarding rules, blame the student.

---
*Source basis: NIST SP 800-61 Rev. 3 (April 2025), CISA Cyber Essentials, CERT-In Directions 28 Apr 2022. Not legal advice; reportability decided by named humans.*
