# AI-Powered Web Security Learning Assistant

**Audience:** Second-year CSE students learning web development  
**Purpose:** Teach defensive secure coding through explanations, safe examples, a checklist, and a small local code-review assistant.

## What is included
- `app/`: Flask learning app with a deterministic defensive code checker and optional AI explanation API.
- `tests/`: unit tests for the local checker.
- `docs/`: research report, ~1,000-word defensive guide, checklist, five code pairs, quiz/answer key, six-slide talk outline, demo script.
- `prompts/`: prompt library for research, code explanation, quiz design, and safe AI review.
- `reports/`: AI verification plan/results template and before/after analysis.
- `assets/`: OWASP Top 10:2025 infographic.
- `.github/workflows/security-check.yml`: runs tests and the local checklist checker on pushes/pull requests.

## Quick start (Windows / macOS / Linux)
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Create a virtual environment:
   - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the app: `python run.py`
6. Open `http://127.0.0.1:5000`.

The demo app is intended for localhost only. It does not run submitted code, send requests to external websites, or generate exploit payloads.

## Optional AI explanation
The AI integration is **off by default**. To enable it, set `OPENAI_API_KEY` in your environment and install the listed `requests` dependency. Then set `AI_ENABLED=1`. The app sends only the code text entered into the review form to the configured API; do not submit secrets, real user data, or proprietary code. Verify all AI output. If no key is set, the local rule-based explanation still works.

The API feature uses the OpenAI Responses API endpoint and a configurable model name (`OPENAI_MODEL`, default `gpt-4.1-mini`). API availability and pricing depend on your account. Never commit API keys to GitHub.

## Safety boundaries
- Use this project only for defensive education and code you own or are authorized to review.
- The checker is a teaching aid, **not** a complete security scanner. It can miss bugs and flag harmless patterns.
- No exploit payloads, attack scripts, remote scanning, or live-target testing are included.
- Practice only in your own local lab or authorized training environments such as OWASP Juice Shop / DVWA.
- Keep dependencies updated and review the current official guidance before submission.

## Automated checks
Run:
```bash
python -m unittest discover -s tests -v
python tools/checklist_scan.py app
```
A non-zero checker exit means one or more heuristic warnings were found; review them manually. A clean result does not prove the application is secure.

## Research sources
- OWASP Top 10:2025: https://owasp.org/www-project-top-ten/
- OWASP Top 10:2025 introduction/categories: https://top10.owasp.org/2025/0x00_2025-Introduction/
- NIST SP 800-218 SSDF v1.1: https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF project (notes draft v1.2 is not final): https://csrc.nist.gov/projects/ssdf
- MDN Web Security: https://developer.mozilla.org/en-US/docs/Web/Security
- MDN Input validation: https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Input_validation
- Flask Security Considerations: https://flask.palletsprojects.com/en/stable/web-security/

## Before submission
1. Run the tests and save the terminal output.
2. If your rubric requires two AI research tools, independently repeat the research prompt in a second tool (e.g., Gemini or Perplexity), record the date, tool, exact prompt, sources, and differences in `reports/ai_verification_report.md`. Do not claim a tool was used unless you actually used it.
3. Add your name, college, department, course, and faculty details to the report and slides.
4. Inspect infographic text carefully; AI-generated graphics can contain typographical inaccuracies.
