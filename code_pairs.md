# Five Insecure-versus-Secure Code Pairs
All examples are intentionally small, defensive teaching snippets. Adapt them to your framework and test them.

## 1. SQL injection: string concatenation vs parameterized query
**Insecure (Python DB-API example):**
```python
query = "SELECT * FROM users WHERE username = '" + username + "'"
cursor.execute(query)
```
**Secure:**
```python
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
```
Use the placeholder syntax required by your database driver. Parameters keep data separate from SQL syntax. Do not build SQL by concatenating untrusted values.

## 2. XSS: unsafe HTML insertion vs text output
**Insecure (JavaScript):**
```javascript
profile.innerHTML = userSuppliedName;
```
**Secure for plain text:**
```javascript
profile.textContent = userSuppliedName;
```
If rich HTML is a genuine requirement, use a maintained, vetted sanitizer and context-specific encoding. `textContent` is suitable for text, not for rendering intended HTML.

## 3. Input validation: unchecked input vs allowlist validation
**Insecure:**
```python
age = int(request.form["age"])  # can raise; no range check
```
**Secure:**
```python
raw_age = request.form.get("age", "")
if not raw_age.isdecimal():
    raise ValueError("Age must be a whole number")
age = int(raw_age)
if not 0 <= age <= 120:
    raise ValueError("Age is outside the accepted range")
```
Validate on the server even when client-side validation exists. Define bounds from real business requirements; validation complements, but does not replace, context-specific SQL/XSS defenses.

## 4. Password storage: fast general hash vs password-hashing function
**Insecure:**
```python
import hashlib
stored = hashlib.sha256(password.encode()).hexdigest()
```
**Secure (Werkzeug example):**
```python
from werkzeug.security import generate_password_hash, check_password_hash
stored = generate_password_hash(password)
ok = check_password_hash(stored, submitted_password)
```
Use a maintained password-hashing library configured with an appropriate password-hashing algorithm and work factor. Never store plain text passwords; general-purpose fast hashes are unsuitable for password storage.

## 5. Access control: trusting an ID vs checking ownership
**Insecure:**
```python
document = get_document(request.args["id"])
return document.body
```
**Secure (illustrative pseudocode):**
```python
document = get_document(document_id)
if document.owner_id != current_user.id:
    abort(403)
return document.body
```
Authentication proves who the user is; authorization checks what they may do. Enforce permissions server-side on every relevant request, including object-level access.
