# Six-slide talk outline

## Slide 1: AI-Powered Web Security Learning Assistant
Target audience: second-year CSE students
Goal: explain common risks and teach safer code
Defensive education only

## Slide 2: Why web security matters
Web apps handle identity, data, and actions
OWASP Top 10:2025 is an awareness starting point
A category list is not a complete security audit

## Slide 3: Five code patterns
SQL: parameterized queries
XSS: safe text output / context-aware encoding
Input: server-side allowlists and bounds
Passwords: password-hashing library
Access: authorize every protected object

## Slide 4: How the assistant works
Student pastes a short code snippet
Local heuristic checker flags selected patterns
Assistant explains risk and defensive next steps
It never executes code or scans remote targets

## Slide 5: Automation and verification
Python scanner + unit tests + GitHub Actions
Check findings manually; scanner has false positives/negatives
Verify claims against OWASP, NIST, MDN, and Flask docs
Compare ChatGPT with a second AI research tool and record real results

## Slide 6: Ethics and conclusion
Practise only in a local lab or authorized training app
Never share secrets or private data with AI
No working exploits or attack tools
AI assists learning; human review and tests decide