# Secure-Coding Checklist (Student Edition)
Use this during design, code review, and before a demo. Mark N/A only with a reason.

## Input and output
- [ ] Validate all inputs on the server using allowlists, type checks, and sensible length/range limits.
- [ ] Use parameterized database queries or a safe ORM; never concatenate untrusted input into SQL.
- [ ] Use safe output APIs (e.g., `textContent`) and context-aware output encoding; sanitize only when rich HTML is required.
- [ ] Treat file uploads, URLs, headers, cookies, JSON, and hidden form fields as untrusted.

## Identity and permissions
- [ ] Store passwords with a maintained password-hashing function (Argon2id, scrypt, bcrypt, or framework-supported equivalent).
- [ ] Use secure session handling; rotate sessions after login and invalidate them on logout where applicable.
- [ ] Check authorization server-side for every protected action and object, not just at the UI.
- [ ] Use MFA/passkeys where appropriate and rate-limit authentication attempts.

## Data and configuration
- [ ] Use HTTPS in deployment; never disable TLS certificate verification to “fix” a connection.
- [ ] Keep secrets out of source control; use environment variables or a secret manager.
- [ ] Disable debug mode and verbose stack traces in production.
- [ ] Set suitable cookie flags (`Secure`, `HttpOnly`, `SameSite`) and review CSRF protections for state-changing requests.
- [ ] Apply least privilege to database accounts, services, and file permissions.

## Dependencies and integrity
- [ ] Pin/review dependencies and remove unused packages.
- [ ] Check advisories and update dependencies using a controlled process.
- [ ] Protect CI/CD secrets and restrict workflow permissions.
- [ ] Verify downloaded artifacts and use integrity controls where appropriate.

## Errors, logging, and resilience
- [ ] Return generic client-facing errors; keep sensitive diagnostics in restricted logs.
- [ ] Log security-relevant events without logging passwords, tokens, or unnecessary personal data.
- [ ] Set request/body/time/resource limits and handle exceptional conditions safely.
- [ ] Add tests for both expected and rejected inputs and for authorization boundaries.

## AI-assisted review
- [ ] Ask AI for defensive explanations and tests, not exploits or attack tooling.
- [ ] Verify each claim against official documentation.
- [ ] Review AI code manually, run tests, and check for outdated APIs.
- [ ] Never paste secrets, private data, or code you are not permitted to share.
- [ ] Record hallucinations, unsafe suggestions, and corrections.
