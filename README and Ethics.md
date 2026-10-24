# Incident Response Playbook Project — README & Ethics Statement

**Prepared by: Pradhiksha**

**Project question:** How can AI help draft and stress-test a simple incident response playbook for a small office or college lab?

## 1. Target audience (Task 1)
**A college lab.** Fictional organisation: **Applied Data Lab (ADL), Greenfield Institute of Technology** (fictional).
- ~25 students, 3 staff, 12 shared workstations, 6 student laptops (BYOD), 1 file server, cloud storage + institute email.
- Why a lab: shared accounts, BYOD, rotating students and thin IT staffing make it a realistic "small office" analogue. India context → CERT-In rules apply (see Research Report).

## 2. Files in this submission
| # | File | Task |
|---|------|------|
| 00 | `00_README_and_Ethics.md` | Ethics (12), tool log, index |
| 01 | `01_Research_Report.md` | 2, 3, 4 (summary) |
| 02 | `02_IR_Checklist_and_Contact_Tree.md` | 4 |
| 03 | `03_Playbook.md` | 5 |
| 04 | `04_Tabletop_Exercise.md` | 6 |
| 05 | `05_Report_Templates.md` | 7 |
| 06 | `06_Quiz_and_Answer_Key.md` | 8 |
| 07 | `07_Briefing_6_Slides.pptx` | 8 |
| 08 | `08_Automation_Guide.md`, `08_incident_to_report.py`, `08_sample_form.json`, `08_sample_output_draft_report.md` | 9 |
| 09 | `09_Prompt_Library.md` | 11 |
| 10 | `10_Verification_Report.md` | 10 |
| 11 | `11_Before_After_Analysis.md` | Final submission |
| 12 | `12_Final_Demo_Script.md` | Final demo |

## 3. AI tool log (be honest — fill in the blanks)
Requirement: **at least 4 free AI tools**. Record what *you* actually ran.

| Tool | Used for | Done in this draft? | You still need to |
|------|----------|---------------------|-------------------|
| Claude (with web search) | Source search, first drafts of all documents, script | **Yes** | Keep screenshots of the chat |
| Perplexity (free) | Second research pass & citation check | **No** — run prompts P1–P2 | Paste answers + screenshots in Verification Report §5 |
| Gemini or ChatGPT (free) | Cross-check / hallucination test | **No** — run prompts V1–V4 | Log results in Verification Report §5 |
| NotebookLM | Upload the 3 source PDFs, ask grounded questions, generate quiz check | **No** | Run prompt N1, log results |
| Gamma | Optional restyle of the slides | Optional | Import the `.pptx` or paste outline |
| Make / Zapier (free tier) | Automation | Blueprint + tested Python equivalent | Build the flow in the guide |

> This package does **not** claim outputs from tools that were not run. Sections that need your own tool runs are marked **[YOU RUN]**.

## 4. Ethics statement (Task 12)
1. **Fictional organisation only.** Greenfield Institute, ADL, all people, hostnames, IPs, phone numbers and email addresses are invented. Real emergency numbers (CERT-In) are public and quoted from the cited source.
2. **No real breach data.** No real victim data, credentials, logs or leaked datasets were used. Scenarios are invented. Sample IPs use documentation ranges (e.g. 203.0.113.x).
3. **AI is an assistant, not an authority.** AI drafts were checked against primary sources. Nothing here is legal advice. Reporting duties (CERT-In, data-protection law, institute policy, police) must be confirmed with the institute's legal/IT officer and current official text.
4. **Human in the loop.** Containment steps that destroy evidence, involve payment, law-enforcement contact or public statements need a named human decision-maker.
5. **Safe-use limits.** The playbook contains defensive steps only. It contains no attack instructions, and the tabletop uses no working malware or exploit details.
6. **Privacy.** Templates tell responders to share the minimum personal data needed and never paste passwords or personal data into public AI tools.
7. **Attribution & honesty.** Sources are cited; where something could not be verified it is flagged. AI use is disclosed in the Prompt Library.
8. **Automation safety.** The automation only creates a *draft* for human review; it never sends external reports itself.
