# Before/After Security Analysis
| Topic | Before (risk pattern) | After (defensive pattern) | Residual checks |
|---|---|---|---|
| SQL | Concatenate user input into SQL | Parameterized query | Correct driver placeholders, least-privilege DB account, tests |
| XSS | Put untrusted text into `innerHTML` | Use `textContent` for plain text; vetted sanitizer for rich HTML | Review template escaping and output context; CSP defense in depth |
| Input | Convert/use input without format/range checks | Server-side allowlist, type and bounds validation | Business-specific rules and resource limits |
| Passwords | Plain text or fast general-purpose hash | Maintained password-hashing library | Work factor, reset flows, MFA/passkeys, rate limits |
| Access control | Fetch record and return it based only on supplied ID | Server-side role/ownership check per request | Test cross-user access and all API routes |

**Important:** This is a conceptual before/after comparison, not proof that a real production system has been remediated. Run regression tests and independent review.
