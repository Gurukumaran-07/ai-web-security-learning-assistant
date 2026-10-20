"""Optional, opt-in AI explanation. Off by default. Never use for secrets or private code."""
import os
import requests

SYSTEM_PROMPT = """You are a defensive secure-coding tutor for beginner web developers.
Explain risks and fixes only. Do not generate exploit payloads, attack scripts, malware,
remote scanning instructions, or attack tools. If asked for those, refuse and redirect to
safe remediation and authorized local practice. Do not claim code is secure from a snippet alone.
Be explicit about uncertainty and recommend official documentation and tests."""

def explain_with_ai(code: str) -> str:
    if os.getenv("AI_ENABLED") != "1":
        return "AI API is disabled. Use the local heuristic findings and official references."
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "AI API is enabled but OPENAI_API_KEY is missing. Configure it securely or leave AI disabled."
    # Keep requests small and avoid submitting secrets/proprietary code.
    if len(code) > 12000:
        return "Snippet is too long for the optional explanation. Submit a smaller excerpt."
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "model": model,
            "instructions": SYSTEM_PROMPT,
            "input": "Review this code defensively. Identify likely issues, safe fixes, and tests. Do not execute it.\n\n" + code
        },
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()
    # Responses API commonly returns output_text; handle missing output safely.
    return data.get("output_text") or "No text returned. Review the API response and official docs."
