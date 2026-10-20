import os
from flask import Flask, request, render_template_string
from app.checker import review_code
from app.ai_explainer import explain_with_ai

app = Flask(__name__)
app.config.update(
    MAX_CONTENT_LENGTH=50_000,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    # Secure=True should be enabled when served over HTTPS in deployment.
)

PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Secure Coding Learning Assistant</title>
<style>
body{font-family:system-ui,Arial;margin:0;background:#0b1220;color:#eaf2ff}
main{max-width:980px;margin:auto;padding:28px}
.card{background:#142238;border:1px solid #28415f;border-radius:14px;padding:20px;margin:16px 0}
textarea{width:100%;min-height:220px;background:#07101d;color:#eaf2ff;border:1px solid #45617e;border-radius:8px;padding:12px;box-sizing:border-box;font:14px monospace}
button{background:#14b8a6;color:#04211f;font-weight:700;border:0;border-radius:8px;padding:12px 18px;cursor:pointer}
small,.muted{color:#b6c6da}.finding{border-left:4px solid #fbbf24;padding:10px;margin:12px 0;background:#1d2b40}
code{color:#7dd3fc}a{color:#7dd3fc}
</style></head><body><main>
<h1>🛡️ Secure Coding Learning Assistant</h1>
<p class="muted">A local-first teaching demo for second-year CSE students. Defensive review only.</p>
<div class="card"><h2>Review your code</h2>
<p>Paste a small snippet you own. This demo never executes code or tests a live website.</p>
<form method="post">
<textarea name="code" maxlength="50000" aria-label="Code to review" placeholder="Paste a short code snippet here...">{{ code }}</textarea><br><br>
<button type="submit">Review code</button>
</form></div>
{% if submitted %}
<div class="card"><h2>Review summary</h2>
<p>Heuristic warnings: <strong>{{ findings|length }}</strong></p>
{% if findings %}
{% for f in findings %}<div class="finding"><strong>{{ f.rule }}</strong> — line {{ f.line }}<br>{{ f.explanation }}</div>{% endfor %}
{% else %}<p>No patterns matched the small teaching rules. This is <strong>not</strong> proof the code is secure; review logic, permissions, dependencies, and tests manually.</p>{% endif %}
<h3>Next steps</h3><ul><li>Read the explanation and compare it with official sources.</li><li>Write a regression test for the fix.</li><li>Do not paste passwords, API keys, personal data, or proprietary code into AI services.</li></ul>
</div>{% endif %}
<div class="card"><h2>What this tool can and cannot do</h2>
<ul><li>Can flag a few suspicious code patterns for learning.</li><li>Cannot understand every program path or prove absence of vulnerabilities.</li><li>Does not create exploit payloads, run code, scan external hosts, or attack systems.</li></ul>
<p>Official reading: <a href="https://owasp.org/www-project-top-ten/">OWASP Top 10</a> · <a href="https://developer.mozilla.org/en-US/docs/Web/Security">MDN Web Security</a></p></div>
</main></body></html>"""

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    findings = []
    submitted = request.method == "POST"
    if submitted:
        code = request.form.get("code", "")
        findings = review_code(code)
    return render_template_string(PAGE, code=code, findings=findings, submitted=submitted)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)


@app.route("/api/explain", methods=["POST"])
def api_explain():
    # Small JSON API for optional AI explanation; localhost demo only.
    from flask import jsonify
    payload = request.get_json(silent=True) or {}
    code = payload.get("code", "")
    if not isinstance(code, str) or len(code) > 12000:
        return jsonify({"error": "Provide a code string of at most 12000 characters."}), 400
    # This API is disabled unless AI_ENABLED=1 and a key is configured.
    try:
        explanation = explain_with_ai(code)
    except Exception:
        # Do not expose internal exception details or credentials.
        return jsonify({"error": "AI explanation failed. Check configuration and logs privately."}), 502
    return jsonify({"explanation": explanation})
