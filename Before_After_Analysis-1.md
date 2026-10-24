# Before / After Analysis

**Prepared by: Pradhiksha**

Compares an **unverified first AI draft** with the **verified final** package. "Before" findings below are real issues caught in this drafting session; the metrics table has blanks for you to fill from your own multi-tool runs.

## 1. Qualitative comparison
| Area | Before (first AI draft / unverified) | After (verified & revised) | Why it matters |
|------|-------------------------------------|-----------------------------|----------------|
| NIST guidance | Described Rev. 2's four phases as "the NIST model" | Cites Rev. 3 (Apr 2025) as current; Rev. 2 labelled legacy; mapping table to the 5-phase teaching model | Outdated standard = wrong training |
| Phase model | Presented Prepare/Detect/Contain/Recover/Review as NIST's | Labelled a simplification | Avoids false attribution |
| Contain advice | "Power off, wipe and reinstall" | Disconnect, preserve evidence, wipe only with approval | Evidence & legal safety |
| Reporting | Vague "report to authorities" | 6-hour CERT-In clock from *noticing*, human decision owner, form worksheet | Compliance timing |
| Contacts | Generic CISA hotline for everyone | CERT-In primary; CISA marked US reference | Geographic correctness |
| Legal tone | Confident "you must/need not report" | "Incident Lead + Institute IT/legal decide; not legal advice" | AI can't give legal rulings |
| Source quality | Mixed blogs and aggregators | Primary sources + secondary corroboration, flagged | Verifiability |
| Process | Static documents | Tabletop scoring sheet, review template, automation draft | Testable, improvable |
| Automation | Idea only | Tested script + Make/Zapier build guide, draft-only | Reduces delay safely |

## 2. Quantitative table **[YOU FILL]**
| Metric | Before | After |
|---|---|---|
| Factual claims checked | | |
| Claims wrong/outdated/unverifiable | (see Verification Report rows 1,2,3,6,7,9 → 6 flagged of 12 checks) | 0 unresolved flagged items remaining as "unverified" without disclosure |
| Unsafe-advice items found | 2 (rows 10, 11) | 0 |
| Time to draft one playbook (min) | | |
| Time to verify one playbook (min) | | |
| Tabletop score avg /12 (dry run) | | |
| Quiz avg score | | |
| Time from form submit → draft report (manual vs automated) | e.g. 20 min | e.g. <1 min |

## 3. What AI did well / badly
**Well:** speed, consistent structure, scenario ideas, red-team style questions, quiz generation, script scaffolding.
**Badly / needs humans:** version currency, authoritative legal statements, region-specific contacts, safe-vs-evidence trade-offs, anything needing primary-document reading.

## 4. Lessons
1. Ask AI for **sources and dates**, then open them.
2. Use a **second tool** and compare disagreements.
3. Give AI the **fictional context and constraints** (who, how big, what rules).
4. Keep AI **draft-only** in automations.
5. Re-run the tabletop after every playbook change.

## 5. Next improvements
- Run the tabletop with real students (fictional scenarios) and log scores.
- Get IT/legal officer sign-off before real adoption.
- Add an incident type: phishing report; add USB-found device.
