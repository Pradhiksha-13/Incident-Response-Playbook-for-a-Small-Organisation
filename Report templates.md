# Report & Communication Templates (fictional organisation: ADL, Greenfield Institute)

> Never paste real personal data, passwords or breach data into AI tools or templates shared outside the institute.

## Template 1 — Incident Report (fill during/after incident)
**Incident ID:** ADL-YYYY-NNN  **Status:** ☐ Open ☐ Contained ☐ Recovered ☐ Closed
**Reported by / role:** ____  **Time noticed (date, 24h, IST):** ____  **Time reported to Incident Lead:** ____
**Type:** ☐ Lost/stolen device ☐ Malware ☐ Account takeover ☐ Other: ____
**Severity:** ☐ Low ☐ Medium ☐ High
**Systems/accounts affected:** ____
**Data involved (types only, no contents):** ☐ none ☐ student ☐ staff ☐ research ☐ credentials ☐ unknown
**What happened (facts only, with times):**
| Time | Event | By whom |
|---|---|---|
**Actions taken (containment):** ____
**Evidence preserved (where stored):** ____
**Reportability decision:** CERT-In ☐ yes ☐ no ☐ pending — decided by ____ at ____ (reason) ; Police ☐ ; Data-protection officer ☐ ; Insurance/vendor ☐
**External report sent (time/reference):** ____
**Recovery steps & verification:** ____
**Open questions:** ____  **Approved by (Incident Lead):** ____

## Template 2 — Internal Notice (staff and students)
**Subject:** [Action needed/For information] ADL IT incident ADL-YYYY-NNN — [short plain description]
> Hello all,
> At **[time, date]** we identified **[brief factual description, e.g., a suspicious email sent from a lab account]**. We are investigating and have **[actions taken, e.g., secured the account and isolated one computer]**.
> **What we know:** [facts]. **What we don't know yet:** [unknowns].
> **What you should do now:** (1) [e.g., do not open the link titled "Shared document"]; (2) [change password at ____ if you entered it]; (3) report anything unusual to **[Tech Lead, ext.]**.
> **What you don't need to do:** [e.g., you do not need to reinstall anything].
> Next update by **[time]**. Please don't forward this outside the lab. Thank you for reporting quickly.
> — [Incident Lead / Comms Lead]

## Template 3 — Message to External Parties (draft only; Institute legal approves)
> Subject: Notice regarding [event] at Applied Data Lab
> We are writing to inform you that on [date] we identified [event]. The information potentially involved is [types]. We have [actions]. We recommend you [actions]. Contact [name/email] for questions. We will update you by [date].
*Do not send without approval of the Institute's legal/IT officer.*

## Template 4 — Regulator / CERT-In Report Worksheet (prepare facts; submit only via official CERT-In format)
Collect: reporting entity & contact · date/time noticed · incident type (per CERT-In Annexure I) · systems affected & IPs/hostnames · timeline · impact · actions taken · logs available. **Submit to CERT-In via incident@cert-in.org.in / 1800-11-4949 using the format published on cert-in.org.in. Within 6 hours of noticing, if reportable.** (Verify current format on the website.)

## Template 5 — Post-Incident Review (blameless; within 5 working days)
**Incident ID:** ____ **Date of review:** ____ **Attendees:** ____
1. **Summary (3 lines):** ____
2. **Timeline (noticed → contained → recovered):** durations: detect ___ min, contain ___ min, recover ___ hrs
3. **What went well:** ____
4. **What went poorly / surprised us:** ____
5. **Root cause(s) and contributing factors:** ____
6. **Was the playbook followed? Gaps?** ____
7. **Reporting decision review (was it timely/correct?):** ____
8. **Action items**
| # | Action | Owner | Due | Done |
|---|---|---|---|---|
9. **Playbook / training / checklist updates needed:** ____
10. **Sign-off:** Incident Lead ____ Dept. Head ____

## Template 6 — Staff/Student "All clear" note
> Subject: ADL incident ADL-YYYY-NNN — resolved
> The incident is resolved as of [time]. Summary: [2 lines]. Changes made: [e.g., MFA now required]. Thank you to those who reported quickly. Questions → [contact].
