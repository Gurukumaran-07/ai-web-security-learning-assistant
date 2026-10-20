# Quiz: Web Security for Beginners
Choose one answer for each question.

1. What is the preferred defense against SQL injection when values are used in SQL?
   A. Hide the query from the browser  B. Parameterized queries  C. Rename the table  D. Use a longer URL

2. Which JavaScript API is generally safer for displaying untrusted plain text?
   A. `innerHTML`  B. `eval`  C. `textContent`  D. `document.write`

3. Why must server-side validation exist even if a form has browser validation?
   A. Browser validation can be bypassed  B. It makes CSS work  C. It encrypts data  D. It replaces authorization

4. Which is a suitable approach for password storage?
   A. Plain text  B. Base64  C. MD5  D. A maintained password-hashing function such as Argon2id/bcrypt/scrypt

5. Authentication answers which question?
   A. What colour is the page?  B. Who is the user?  C. Which CSS file loads?  D. How big is the database?

6. Authorization checks:
   A. What the authenticated user is allowed to do  B. Whether JavaScript is enabled  C. The user's screen size  D. Whether a package is popular

7. What should developers do with API keys?
   A. Commit them to GitHub  B. Put them in HTML  C. Keep them in secret management/environment configuration  D. Print them in logs

8. What is the best response to an AI claim that cites a security API you cannot find?
   A. Trust it because it sounds confident  B. Verify with official documentation and test safely  C. Deploy immediately  D. Delete all tests

9. What does a clean result from this project's heuristic scanner mean?
   A. The app is guaranteed secure  B. No configured patterns matched; manual review is still needed  C. It has no bugs  D. It is safe to deploy

10. Where should students practise security checks?
   A. Any public website  B. A stranger's server  C. Their own local lab or explicitly authorized training environment  D. Random IP addresses

## Answer key with explanations
1. B — Parameterization separates data from SQL syntax.
2. C — `textContent` inserts text rather than parsing it as HTML.
3. A — Attackers can send requests without using the page's form controls.
4. D — Password-specific hashing is designed to make guessing more costly.
5. B — Authentication verifies identity.
6. A — Authorization determines allowed actions and resources.
7. C — Keep secrets out of source control and client-side code.
8. B — Confirm claims using primary documentation and controlled tests.
9. B — Heuristic scanners are incomplete and can miss vulnerabilities.
10. C — Only test systems you own or have explicit permission to test.
