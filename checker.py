"""Small educational heuristic checker. It does not execute code or prove security."""
import re

RULES = [
    ("SQL query concatenation", re.compile(r"(SELECT|INSERT|UPDATE|DELETE).{0,160}(\+\s*\w+|f['\"])", re.I | re.S),
     "Possible SQL query construction with string concatenation/interpolation. Prefer parameterized queries or a well-configured ORM."),
    ("Unsafe HTML insertion", re.compile(r"\.innerHTML\s*=", re.I),
     "Potential unsafe HTML insertion. Prefer textContent for plain text; if rich HTML is required, use a vetted sanitizer and context-aware design."),
    ("Hard-coded secret", re.compile(r"(api[_-]?key|secret|password|token)\s*=\s*['\"][^'\"]{5,}['\"]", re.I),
     "Possible hard-coded secret. Move secrets to environment/secret management and rotate any real exposed credential."),
    ("Weak hash primitive", re.compile(r"\b(md5|sha1)\s*\(", re.I),
     "MD5/SHA-1 are not appropriate for password storage. Use a password-hashing function such as Argon2id, scrypt, or bcrypt via a maintained library."),
    ("Debug mode enabled", re.compile(r"debug\s*=\s*True", re.I),
     "Debug mode appears enabled. Disable debug mode outside isolated development; do not expose debugger in a deployed app."),
    ("Disabled TLS verification", re.compile(r"verify\s*=\s*False", re.I),
     "TLS certificate verification may be disabled. Keep certificate verification enabled and fix the trust configuration instead."),
]

def review_code(code: str):
    findings = []
    for title, pattern, explanation in RULES:
        for match in pattern.finditer(code):
            line = code.count("\n", 0, match.start()) + 1
            findings.append({
                "rule": title,
                "line": line,
                "severity": "Review",
                "explanation": explanation
            })
    return findings
