"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (<200 chars) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
"""

from pathlib import Path

PITCH = (
    "A subscription that writes 'sorry, I was offline' excuses for lazy AI "
    "agents that miss their human's 9am deadlines - $3 a month, auto-billed "
    "to the human who never reads the invoice."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
