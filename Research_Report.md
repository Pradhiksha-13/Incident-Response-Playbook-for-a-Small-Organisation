# Research Report — AI-Assisted Incident Response Playbook for a Small College Lab

**Audience:** Applied Data Lab (ADL), Greenfield Institute of Technology (fictional) · **Date:** 24 Oct 2026

## 1. Research question
How can AI help draft and stress-test a simple incident response (IR) playbook for a small office or college lab — and where must humans step in?

## 2. Method
1. Searched official/primary sources for NIST, CERT-In and CISA (Claude with web search; **[YOU RUN]** Perplexity + NotebookLM passes — see Prompt Library P1, P2, N1).
2. Preferred primary/government sources; law-firm explainers used only as secondary confirmation.
3. Cross-checked each claim; logged results in `10_Verification_Report.md`.

## 3. Verified source list
| ID | Source | Type | What it supports | Status |
|----|--------|------|------------------|--------|
| S1 | NIST SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile* — https://csrc.nist.gov/pubs/sp/800/61/r3/final | Primary (US gov) | Current IR guidance; finalised April 2025; supersedes Rev. 2 | ✅ Verified (NIST news notice, 3 Apr 2025) |
| S2 | NIST news notice "NIST Revises SP 800-61" — https://csrc.nist.gov/news/2025/nist-revises-sp-800-61 | Primary | Confirms Rev. 3 supersedes Rev. 2; all six CSF 2.0 Functions play a role in IR | ✅ |
| S3 | CERT-In Directions No. 20(3)/2022-CERT-In, 28 Apr 2022 — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf | Primary (India gov) | 6-hour reporting; contact channels | ✅ via multiple secondary summaries; **[YOU]** open the PDF and confirm Annexure I yourself |
| S4 | CERT-In website — https://www.cert-in.org.in | Primary | Current reporting format/forms ("updated from time to time") | **[YOU]** check live |
| S5 | CISA Cyber Essentials — https://www.cisa.gov/publication/cisa-cyber-essentials and https://www.cisa.gov/small-business | Primary (US gov) | Six essential elements incl. "Your Crisis Response"; small-business resources | ✅ |
| S6 | CISA blog "Celebrating Small Business Week" (May 2022) | Primary | Advice to write an IR plan and run exercises | ✅ |
| S7 | Law-firm summaries (Linklaters, Trilegal, Mondaq) | Secondary | Cross-check of CERT-In facts | ✅ used only to corroborate |

## 4. Key findings

### 4.1 NIST SP 800-61 — the framework changed
- **Rev. 3 (April 2025) replaced Rev. 2 (2012).** It frames IR as part of overall cybersecurity risk management and is a *Community Profile of CSF 2.0*, tying IR to all six CSF Functions: Govern, Identify, Protect, Detect, Respond, Recover. (S1, S2)
- Rev. 2's classic life cycle was 4 phases: *Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity* (from NIST Rev. 2; widely known — still useful for teaching).
- **Implication:** The brief's five phases (**Prepare, Detect, Contain, Recover, Review**) are a *teaching simplification*, not NIST's official wording. Our playbook maps them explicitly:

| Project phase | NIST Rev. 2 (legacy) | NIST Rev. 3 / CSF 2.0 |
|---|---|---|
| Prepare | Preparation | Govern, Identify, Protect (ongoing) |
| Detect | Detection & Analysis | Detect (+ Respond: analysis) |
| Contain | Containment, Eradication | Respond |
| Recover | Recovery | Recover |
| Review | Post-incident activity | Lessons learned feed improvement across all Functions |

### 4.2 CERT-In (India) — a hard clock
- Directions dated **28 April 2022** under s.70B(6) IT Act; effective **27 June 2022**. (S3, S7)
- Service providers, intermediaries, data centres, **body corporates and government organisations** must report listed cyber incidents **within 6 hours** of noticing or being notified. (S3)
- Channels stated in the Directions: **incident@cert-in.org.in**, phone **1800-11-4949**, fax 1800-11-6969; reporting formats are published on cert-in.org.in and may change. (S3)
- Annexure I lists **20 incident types** (per law-firm summaries). Whether a given lab incident is reportable depends on the annexure and institute status → **escalate to the institute's IT/legal officer; do not decide alone and do not let AI decide.**
- Caution: commentators note the 6-hour window is hard for small entities; the Directions also contain other duties (e.g., log retention) not covered in this simple playbook. **[Verify against primary text.]**

### 4.3 CISA small-business resources (US reference, adaptable)
- Cyber Essentials has **six essential elements**: strategy/culture; awareness; protect critical assets; access control; backups; **limit damage and quicken restoration (crisis response)**. (S5)
- Crisis-response actions include leading an incident-response and disaster-recovery plan and "learn who to call for help." (S5)
- CISA advises writing an IR plan and **practising it with exercises**. (S6) → justifies our tabletop.
- CISA's 24/7 contact is for **US** organisations; ADL's primary national contact is CERT-In.

## 5. How AI helped — and where it needs guardrails
| Task | AI strength | Risk found/expected | Human control |
|------|-------------|---------------------|---------------|
| Research | Fast source discovery; summarising | Outdated version (Rev. 2 cited as current); fabricated URLs | Open every link; check publication date |
| Drafting playbooks | Structure, plain language, consistency across 3 incidents | Over-generic or unsafe steps (e.g. "wipe the device immediately", "pay the ransom") | Review by IT lead; check vs NIST/CERT-In |
| Scenario design | Creative injects, varied difficulty | Unrealistic tech detail | Facilitator pre-read |
| Stress-testing | Plays "red team" reviewer; finds gaps (who has authority? 6-hour clock?) | Confident but wrong answers | Cross-check with 2nd tool + source |
| Automation | Generates flow logic/script | Silent data leakage to third parties | Draft-only, minimum data, human approval |
| Quizzing | Fast question banks | Ambiguous keys | Verify answers against playbook |

## 6. Conclusion
AI is most useful as a **drafting partner and adversarial reviewer**, not as the authority. The three biggest corrections made by verification were: (1) NIST Rev. 2 → Rev. 3 currency, (2) the five-phase model is a simplification, (3) reportability and legal duties must be decided by named humans with the primary text. Details in `10_Verification_Report.md`.

## 7. References
- NIST. *SP 800-61 Rev. 3.* April 2025. https://csrc.nist.gov/pubs/sp/800/61/r3/final
- NIST CSRC. "NIST Revises SP 800-61." 3 Apr 2025. https://csrc.nist.gov/news/2025/nist-revises-sp-800-61
- CERT-In. *Directions under s.70B(6) IT Act*, 20(3)/2022-CERT-In, 28 Apr 2022. https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf
- CISA. *Cyber Essentials.* https://www.cisa.gov/publication/cisa-cyber-essentials ; CISA small business page https://www.cisa.gov/small-business
- Linklaters (May 2022), Trilegal (4 May 2022), Mondaq summaries of the CERT-In Directions (secondary).
