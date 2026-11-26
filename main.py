import os

LINE = "I have no idea what I'm doing, but the confidence slider is stuck at one hundred percent."

LIMIT = 200
if len(LINE) != 89 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 89 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
