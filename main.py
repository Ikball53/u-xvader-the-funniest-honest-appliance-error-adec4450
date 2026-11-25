"""Entry for make.fun — The Funniest Honest Appliance Error.

Writes a single honest washing-machine error line to entry.txt.
"""

from pathlib import Path
import os

LINE = "ERROR E04: Load unbalanced. I spent 12 minutes trying to spin one hoodie. It won. I'm not moving until you open the door."

# The brief caps the line at 200 characters, and it must not be empty.
# One line, no trailing spaces: the judge reads entry.txt verbatim.
assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {target}")

if __name__ == "__main__":
    main()
