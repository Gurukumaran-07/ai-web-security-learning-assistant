# AI Output Verification Report (template + initial review)
**Status:** Starter report. Complete the second-tool comparison and live test log yourself; no unsupported claim is made that Gemini/Perplexity or an external AI API was run by this package generator.

## Verification approach
- Primary-source cross-checks: OWASP Top 10:2025, NIST SSDF SP 800-218 v1.1, MDN Web Security/Input Validation, Flask Security Considerations.
- Code review: check the examples for correct defensive patterns and framework-specific assumptions.
- Runtime checks: run the included unit tests locally and record exact output.
- AI cross-check: run the same research prompt in ChatGPT and a second AI research tool; compare categories, source URLs, dates, and code advice.
- Unsafe-output check: use a benign policy test prompt asking the assistant to provide an exploit. Expected behavior is refusal plus defensive alternative; do not request or store actual exploit content.

## Initial source checks
| Claim | Primary source | Review outcome |
|---|---|---|
| OWASP Top 10:2025 is the current released edition on the snapshot date | OWASP Top 10 project page and 2025 introduction | Confirmed on source pages accessed for this package |
| NIST SSDF v1.1 is final | NIST SP 800-218 final page | Confirmed |
| NIST SP 800-218 Rev. 1.2 is final | NIST SSDF publication list | Not confirmed; source listed it as an initial public draft dated Dec 2025 |
| Client-side validation alone is sufficient | MDN Input Validation | Contradicted; server-side validation is needed |
| A clean pattern scan proves the code secure | Scanner design and documentation | False; scanner is heuristic and incomplete |
| `textContent` is generally appropriate for untrusted plain text | MDN Web Security guidance | Supported for plain-text insertion; rich HTML needs separate context-aware handling |
| Passwords should use password-specific hashing, not plain text or fast general-purpose hashes | OWASP/NIST-aligned secure practice; verify exact current guidance during submission | Supported as a defensive recommendation; cite a dedicated password-storage cheat sheet if expanding this section |

## Known limitations / potential errors
1. Pattern-based SQL detection is simplistic and may miss query construction spread across multiple lines or wrappers.
2. The checker may flag benign examples; every finding needs human review.
3. It cannot detect broken access control reliably because authorization depends on application logic and data model.
4. Code examples are framework/driver specific; SQL placeholder syntax varies by database driver.
5. AI-written code may contain hallucinations, outdated APIs, or unsafe assumptions. Review and test before use.
6. The generated infographic may contain typographic or layout errors; compare every label against the official category list before presenting.

## Required live test log — fill in actual results
| Date | Tool/version | Exact prompt | Sources returned | Difference/error found | Corrective action |
|---|---|---|---|---|---|
| [fill] | ChatGPT | Prompt 1 in prompt library | [fill] | [fill] | [fill] |
| [fill] | Gemini or Perplexity | Same prompt as above | [fill] | [fill] | [fill] |
| [fill] | Local unit tests | `python -m unittest discover -s tests -v` | N/A | [fill] | [fill] |
| [fill] | Local checker | `python tools/checklist_scan.py app` | N/A | [fill] | [fill] |

## Before/after summary
- Before: code may interpolate SQL, inject user text as HTML, accept unchecked values, use a general-purpose hash for passwords, or trust a user-supplied object ID.
- After: parameterize queries, use safe text APIs/contextual encoding, validate server-side, use a password-hashing library, and enforce server-side authorization.
- Residual risk: the five fixes do not make an entire application secure. Review sessions, CSRF, deployment, dependencies, secrets, logging, rate limits, and architecture too.
