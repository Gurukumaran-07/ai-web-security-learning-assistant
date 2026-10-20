"""Heuristic checklist scanner for source files; educational only."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app.checker import review_code

EXTS = {".py", ".js", ".ts", ".html", ".jsx", ".tsx"}
SKIP = {".venv", "node_modules", ".git", "__pycache__"}

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    total = 0
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTS:
            continue
        if any(part in SKIP for part in path.parts):
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        findings = review_code(content)
        for item in findings:
            total += 1
            print(f"[REVIEW] {path}:{item['line']} {item['rule']} — {item['explanation']}")
    if total == 0:
        print("No configured patterns matched. This is not a security certification.")
    else:
        print(f"\n{total} review warning(s). Manually verify each finding.")
    return 1 if total else 0

if __name__ == "__main__":
    raise SystemExit(main())
