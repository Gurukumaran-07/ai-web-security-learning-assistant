# Final Demo Script (5–7 minutes)
1. State the target audience and project goal.
2. Open the local app at `http://127.0.0.1:5000`.
3. Paste a harmless teaching snippet containing `element.innerHTML = userInput`; click Review. Explain the warning.
4. Replace it with `element.textContent = userInput`; review again and explain that no match is not a security guarantee.
5. Show `docs/code_pairs.md` and explain parameterized SQL and authorization checks.
6. Run unit tests: `python -m unittest discover -s tests -v`.
7. Run the checklist scanner: `python tools/checklist_scan.py app`.
8. Show the OWASP infographic, quiz, and six-slide deck.
9. Explain AI verification: primary sources, second-tool comparison, hallucination checks, and limitations.
10. Close with ethics: local/authorized testing only; no exploits; never share secrets with AI.
