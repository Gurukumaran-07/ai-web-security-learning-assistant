import unittest
from app.checker import review_code

class CheckerTests(unittest.TestCase):
    def test_flags_inner_html(self):
        findings = review_code("element.innerHTML = userInput")
        self.assertTrue(any(x["rule"] == "Unsafe HTML insertion" for x in findings))

    def test_flags_hardcoded_secret(self):
        findings = review_code("api_key = 'abcde12345'")
        self.assertTrue(any(x["rule"] == "Hard-coded secret" for x in findings))

    def test_flags_debug(self):
        findings = review_code("app.run(debug=True)")
        self.assertTrue(any(x["rule"] == "Debug mode enabled" for x in findings))

    def test_safe_text_content_not_flagged_as_html(self):
        findings = review_code("element.textContent = userInput")
        self.assertFalse(any(x["rule"] == "Unsafe HTML insertion" for x in findings))

if __name__ == "__main__":
    unittest.main()
