# A Beginner’s Guide to Safer Web Code
**Audience:** Second-year CSE students learning web development

## Why secure coding matters
Web applications accept data, identify users, access databases, and expose functions over networks. A small coding mistake can expose private information or let a user perform an action they are not allowed to perform. OWASP Top 10:2025 is an awareness document describing ten important categories of web application risk. It is a starting point, not a complete list of every possible weakness and not a substitute for threat modeling or testing.

## 1. SQL injection
SQL injection can happen when an application joins untrusted input directly into a database query. The database may interpret part of the input as query syntax instead of data. A safer pattern is to use parameterized queries or a well-configured ORM. The database driver binds values separately from the query structure. Input validation remains useful, but it is not a replacement for parameterization. Also use a database account with only the permissions the application needs, and test query behavior with ordinary and invalid inputs in a local test database.

## 2. Cross-site scripting (XSS)
XSS is a class of issue where untrusted content is interpreted as executable browser content in a page. The right defense depends on the output context. For plain text, APIs such as JavaScript `textContent` avoid treating the value as HTML. Template engines often escape text by default, but developers must understand when escaping is disabled. If a product genuinely supports rich HTML, use a maintained sanitizer with an explicit policy. A Content Security Policy can add defense in depth, but it does not replace safe rendering. Test using harmless sample strings in your own local app; do not build or distribute exploit payloads.

## 3. Input validation
Validation checks whether an input matches expected type, format, and business rules. For example, an age field might need to be a whole number in an allowed range. Prefer allowlists: define acceptable values and reject unexpected ones. Validate on the server because client-side checks can be bypassed. Validate early and give helpful error messages without exposing internal details. Validation alone cannot safely neutralize every dangerous input in every context; pair it with the correct SQL, HTML, file-upload, or command-specific defense.

## 4. Password storage and authentication
Passwords should never be stored in plain text or protected with a fast general-purpose hash such as SHA-256 alone. Use a maintained password-hashing implementation designed to slow guessing, such as Argon2id, scrypt, or bcrypt, with appropriate parameters. Do not invent your own password storage scheme. Authentication verifies identity; authorization decides what that identity may access. Use secure session management, protect cookies, rate-limit login attempts, and consider multi-factor authentication or passkeys. Avoid leaking whether a particular account exists through overly specific login errors.

## 5. Broken access control
An application may correctly log a user in but still fail to check whether they are allowed to read or change a particular record. Never trust an ID supplied by a URL or form as proof of permission. Check authorization on the server for every sensitive action and every object, including API routes. A common safe design fetches the requested object, checks the current user's role or ownership, and only then returns or changes it. Test with two test accounts and confirm that one account cannot access the other's private sample data.

## 6. Security misconfiguration
Default passwords, exposed debug pages, overly broad CORS rules, verbose errors, and missing security headers can increase risk. Use secure defaults, keep development and production configuration separate, disable debug mode in deployment, and reveal only generic errors to users. Use HTTPS and configure cookie attributes such as `Secure`, `HttpOnly`, and `SameSite` appropriately. Security headers like Content Security Policy should be tailored and tested; copying a header blindly can break an application or give a false sense of security.

## 7. Software supply-chain failures
Web apps rely on frameworks, libraries, packages, build systems, and CI workflows. A vulnerable or untrusted dependency can affect the whole application. Keep a clear dependency inventory, review advisories, update deliberately, remove unused packages, and protect repository and CI secrets. Lock or pin dependencies in a reproducible way when suitable for the ecosystem. Do not assume a package is safe just because it is popular, and do not install code from untrusted sources without review.

## 8. Cryptographic failures
Sensitive information must be protected in transit and, where appropriate, at rest. Use HTTPS with valid certificate verification, approved cryptographic libraries, and suitable key management. Never hard-code real secrets in source code or commit them to a public repository. Do not design your own encryption algorithm. Use password hashing for passwords; encryption and hashing solve different problems. Review how keys are created, stored, rotated, and accessed.

## 9. Logging, errors, and exceptional conditions
Applications should handle errors predictably. A detailed stack trace may help a developer locally but can reveal paths, queries, versions, or secrets to a user. Return generic client errors and record necessary diagnostic information in access-controlled logs. Logs should not contain passwords, session tokens, or unnecessary personal data. Log relevant security events, protect log access, and define how someone will respond to alerts. Set sensible size and time limits so unusual requests do not exhaust resources.

## 10. How to use AI responsibly
AI can explain code, suggest safer patterns, draft tests, and help beginners compare alternatives. However, AI may invent APIs, recommend deprecated practices, miss authorization logic, or confidently misstate a security claim. Ask for sources and defensive fixes, then verify claims against official OWASP, NIST, MDN, and framework documentation. Compile and test suggested code in a local environment; use peer or instructor review for important changes. Do not paste credentials, private data, or code you are not allowed to share. The assistant in this project uses a small heuristic checker, so its output is only a learning signal: it can produce false positives and false negatives.

## Safe practice rules
Practice only on code you own, an isolated local lab, or authorized educational applications such as OWASP Juice Shop or DVWA. This project does not include working exploits, payload generation, remote scanning, or attack automation. The purpose is to understand risks and prevent them.

## Conclusion
Safer code comes from layers: safe framework defaults, validation, parameterized queries, contextual output handling, authorization checks, secure configuration, dependency management, testing, and careful operations. AI is a learning aid, not an authority. Verify every important suggestion and make security part of the development process from the beginning.
