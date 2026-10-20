# Research Summary: AI-Powered Web Security Learning Assistant
**Audience:** Second-year CSE students learning web development  
**Research snapshot:** 20 October 2026 (verify all links and release status again before final submission)

## Objective
Explore how AI can help beginners identify common web security mistakes, understand why they matter, and adopt defensive fixes without generating attack tools.

## Key findings
1. **OWASP Top 10:2025** is the current released OWASP Top 10 edition identified on the official project page at the research snapshot. It is an awareness document. Its categories are: A01 Broken Access Control; A02 Security Misconfiguration; A03 Software Supply Chain Failures; A04 Cryptographic Failures; A05 Injection; A06 Insecure Design; A07 Authentication Failures; A08 Software or Data Integrity Failures; A09 Security Logging & Alerting Failures; A10 Mishandling of Exceptional Conditions.
2. **NIST SSDF SP 800-218 v1.1** recommends integrating secure development practices into the software development lifecycle to reduce vulnerabilities and address their root causes. The NIST SSDF page also lists a Rev. 1.2 initial public draft dated December 2025; this should not be described as a final standard unless the official status changes.
3. **MDN Web Security** recommends practices including HTTPS, Content Security Policy, cookie protections, input validation, output encoding/sanitization, strong authentication, and dependency control. MDN notes that client-side validation is not enough because requests can bypass the browser UI.
4. **Flask Security Considerations** discusses XSS, CSRF, security headers, cookie flags, and resource limits. Framework guidance must be applied to the version and configuration actually used.
5. **AI's appropriate role** is to explain a warning in beginner language, propose defensive code, suggest regression tests, and link to primary sources. AI output must not be treated as verified fact by itself.
6. **Limitations**: static pattern checks are incomplete; secure code depends on context, architecture, framework versions, permissions, deployment, and tests.

## Recommended research workflow using two AI research tools
Use ChatGPT and a second tool such as Gemini or Perplexity. Give both the same research prompt from `prompts/prompt_library.md`. Record the actual date, tool/version if visible, sources returned, disagreements, and how each claim was verified. This report does not claim that a second tool was actually run; complete that comparison yourself if required by the course.

## Secure-coding recommendations
- Parameterize SQL values.
- Use safe output APIs and context-aware escaping.
- Validate all inputs server-side using allowlists and sensible bounds.
- Use maintained password-hashing libraries.
- Enforce server-side authorization for every protected object/action.
- Keep secrets out of source control.
- Use HTTPS and safe cookie/session configuration.
- Keep dependencies reviewed and updated.
- Return generic client errors; protect logs and avoid recording secrets.
- Test fixes and document false positives/false negatives.

## Primary sources
- OWASP Top 10:2025: https://owasp.org/www-project-top-ten/
- OWASP Top 10:2025 introduction: https://top10.owasp.org/2025/0x00_2025-Introduction/
- NIST SP 800-218 SSDF v1.1: https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF project and publication status: https://csrc.nist.gov/projects/ssdf
- MDN Web Security: https://developer.mozilla.org/en-US/docs/Web/Security
- MDN Input validation: https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Input_validation
- Flask Security Considerations: https://flask.palletsprojects.com/en/stable/web-security/
