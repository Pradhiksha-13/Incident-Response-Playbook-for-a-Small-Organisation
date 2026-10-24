# Automation — Incident Form → Draft Incident Report

**Goal:** When someone submits the incident form, automatically create a **draft** report (and notify the Incident Lead) for human review.
**Safety rules:** fictional/test data only while learning; draft-only (no auto-send to regulators/external); collect the minimum data; no passwords in the form.

## What's included and tested
| File | Purpose | Status |
|---|---|---|
| `08_sample_form.json` | Example form submission (fictional) | ✅ |
| `08_incident_to_report.py` | Local script doing the same logic as the no-code flow | ✅ Run and tested here (output: `08_sample_output_draft_report.md`) |
| This guide | Click-by-click Make/Zapier build | ⚠ **[YOU BUILD]** — not executed in this environment; screenshot your run for the demo |

## Option A — Make.com (free plan)
1. **Form:** Create a Google Form with fields: reporter name, role, time noticed, incident type (dropdown: Lost or stolen laptop / Malware alert / Account takeover / Other), systems affected, data involved (checkboxes), description, actions taken. Link it to a Google Sheet.
2. **Scenario → Module 1:** *Google Sheets → Watch New Rows*.
3. **Module 2:** *Tools → Set variable* `deadline` = `addHours(parseDate(timeNoticed); 6)`.
4. **Module 3 (Router):** three routes by `incident_type` (Lost laptop / Malware / Account takeover) + fallback. Each route *Set variable* `next_steps` with the matching playbook lines (copy from `08_incident_to_report.py`).
5. **Module 4:** *Google Docs → Create a Document from a Template* using Template 1 (file 05) with placeholders `{{reporter}}`, `{{type}}`, `{{time}}`, `{{deadline}}`, `{{steps}}`; title prefix **DRAFT**.
6. **Module 5:** *Gmail/Email → Send an email* **to the Incident Lead only** (internal) with the doc link and the line "Human review required; reporting decision pending."
7. **Test** with `08_sample_form.json` values. Turn scenario *off* when done.

## Option B — Zapier (free plan)
Trigger *Google Forms/Sheets – New Response* → *Formatter – Date/Time: Add 6 hours* → *Paths* (by incident type) → *Google Docs – Create Document from Template* → *Gmail – Send Email* (internal, draft notice).
*(Free plan limits paths/steps; if blocked, use one path with a Formatter lookup table.)*

## Optional AI step (only if you add one)
Add an AI module to summarise the description in 2 lines. Rules: send **no personal data**, mark output "AI-summary — verify", never let it choose severity or reportability. Log the prompt in the Prompt Library.

## Risk check
| Risk | Control |
|---|---|
| Auto-sending sensitive info externally | Only internal email to Incident Lead |
| Personal data in third-party tools | Minimum fields, fictional data in the project, institute approval before real use |
| Wrong severity/type | Rule-based suggestion labelled "confirm" |
| False sense of compliance | Draft states reporting decision requires humans and shows the 6-hour clock |
| Flow breaks silently | Error handler emails Tech Lead |

## Test cases to run (record pass/fail in Verification Report)
1. Malware sample (given) → severity High, deadline +6 h ✅ (script verified)
2. Lost laptop with `data_involved: none` → Low/Medium
3. Missing required field → flow should error and alert
4. Timezone: form in IST vs. server UTC — confirm the deadline displays correctly
