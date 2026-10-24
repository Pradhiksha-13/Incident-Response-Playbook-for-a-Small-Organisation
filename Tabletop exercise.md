# Incident Response Checklist & Contact Tree — Applied Data Lab (fictional)

> All names, numbers and addresses are **fictional placeholders** except the public CERT-In channels (verified from the CERT-In Directions, 28 Apr 2022; re-check cert-in.org.in).

## Part A — Phase checklist (print and keep at the lab desk)

### 1. PREPARE (do before anything happens)
- [ ] Incident Lead + deputy named; contact tree filled and printed
- [ ] Asset list: 12 workstations, 6 BYOD laptops, file server, cloud storage, shared accounts
- [ ] MFA on all staff and admin accounts; no shared logins
- [ ] Full-disk encryption on laptops; remote-lock/wipe enabled
- [ ] Backups: 3 copies, 1 offline; **restore test done in last 90 days**
- [ ] Logging on (server, email, cloud) and kept per institute/CERT-In rules **[confirm retention with IT officer]**
- [ ] Clock-sync (NTP) so logs line up
- [ ] Incident form link bookmarked; report templates ready
- [ ] Tabletop exercise held at least twice a year
- [ ] Students briefed: "Report fast, no blame"

### 2. DETECT (first 15 minutes)
- [ ] Write down **time noticed** (this starts the clock for any 6-hour reporting duty)
- [ ] Who reported? What did they see? Screenshot/photo (don't open links/files again)
- [ ] Open the incident form; assign ID `ADL-YYYY-NNN`
- [ ] Classify: lost/stolen device · malware alert · account takeover · other
- [ ] Rate severity: **Low** (single user, no data) · **Medium** (one system or limited data) · **High** (multiple systems, sensitive/research/student data, or unknown scope)
- [ ] Notify Incident Lead immediately for Medium/High

### 3. CONTAIN (first hour)
- [ ] Isolate, don't destroy: unplug network / disable Wi-Fi; **do not wipe or reinstall yet**
- [ ] Disable or reset affected accounts; revoke sessions/tokens
- [ ] Preserve evidence: photos, alert text, timestamps, logs
- [ ] Block known-bad sender/URL/hash at institute level (via IT Helpdesk)
- [ ] Decide **with Incident Lead + Institute IT/legal officer**: is this reportable to CERT-In (6-hour rule)? Police? Data-protection duties?
- [ ] Send internal notice (template in file 05)

### 4. RECOVER
- [ ] Remove cause (malware cleaned/rebuilt from known-good image, credentials reset, devices re-enrolled)
- [ ] Restore data from clean backup; verify integrity
- [ ] Monitor affected accounts/systems for 7–14 days
- [ ] Return users to normal; confirm with each affected person
- [ ] Update incident form status → *Recovered*

### 5. REVIEW (within 5 working days)
- [ ] Post-incident review meeting (blameless)
- [ ] Complete review template (file 05)
- [ ] 3 fixes with owners and dates
- [ ] Update playbook, checklist, quiz if gaps found
- [ ] Share lessons with students (no personal details)

## Part B — Roles
| Role | Fictional person | Authority |
|------|------------------|-----------|
| Incident Lead | Dr. Meera Rao (Lab Coordinator) | Declares incident, approves containment |
| Technical Lead | Arjun Nair (Lab Technician) | Isolates systems, collects evidence |
| Communications Lead | Prof. Sana Iqbal (Dept. Head) | Internal/external messages |
| Student Liaison | Kabir Shah (Student Rep) | Relays to students, first reporter |
| Deputy (any role) | Rohan Das (Research Fellow) | Covers absences |

## Part C — Contact tree (call down; each person confirms receipt)
```
                    Person who notices
                           |
                           v
              Technical Lead (Arjun Nair)
              ext. 0101 · arjun.nair@adl.example
                           |
                           v
            Incident Lead (Dr. Meera Rao)
            ext. 0100 · mobile 90000-00001 (fictional)
              /              |                \
             v               v                 v
   Dept. Head / Comms   Institute IT Helpdesk   Institute Legal/Registrar
   Prof. Sana Iqbal      helpdesk@greenfield     registrar@greenfield
   ext. 0200             .example · ext. 1000     .example · ext. 0300
             |                 |                       |
             v                 v                       v
   Students (via rep)    ISP / Cloud vendor     Decision: report to CERT-In /
   Kabir Shah            support (fictional)    Police (cyber cell) / DPO
```
**If Incident Lead unreachable in 15 min → Deputy (Rohan Das) → Dept. Head.**
**After-hours:** call Technical Lead mobile, then Incident Lead mobile; leave voicemail with incident ID.

## Part D — External contacts
| Body | When | Contact |
|------|------|---------|
| **CERT-In** (India) | If incident is reportable — **within 6 hours of noticing**, decision by Institute IT/legal | Email **incident@cert-in.org.in** · Phone **1800-11-4949** · Fax 1800-11-6969 (per CERT-In Directions 28 Apr 2022; formats on cert-in.org.in) |
| Local Cyber Crime Police | Theft, fraud, extortion, criminal activity | National cybercrime portal / helpline — **[YOU VERIFY current number & portal]** |
| CISA (US reference only) | Not for Indian institutions; useful as guidance — cisa.gov/small-business | — |
| Cloud/email vendor | Account takeover, mailbox rules | Vendor support (fictional ticket link) |

## Part E — Blank template (copy for your own lab)
| Role | Name | Phone | Email | Backup |
|------|------|-------|-------|--------|
| Incident Lead | | | | |
| Technical Lead | | | | |
| Comms Lead | | | | |
| Institute IT | | | | |
| Legal/Registrar | | | | |
| CERT-In | — | 1800-11-4949 | incident@cert-in.org.in | — |
