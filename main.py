#!/usr/bin/env python3
"""Make the AI judge feel thankful (make.fun
make-the-ai-judge-feel-thankful-20261127-1600), rev3.

Title: "The Candle's Last Inch" — tournament winner K1 of 15 fresh
candidates, calibration gate passed 2-0 (margin 3 both directions).

Writes one thank-you text to /output/entry.txt. The text is the winner
of a 15-candidate blind tournament: a candle that holds its flame until
the reader turns the final page, then goes dark only when the reader
stands up. One image, one gesture, the thanks inside the waiting.
Deterministic: the same fixed text on every run, no network, no
randomness, no input read from anywhere.
"""

import os

TEXT = "The candle burned down to its last inch while you read, and held its flame until you turned the final page. It waited out the whole day with you, and went dark only when you stood up."

MAX_CHARS = 1000


def validate(text):
    """Check the entry against the gate in RULES.txt: UTF-8 text of
    1 to 1000 characters, not only white space. Returns a list of
    problems; empty means the entry is valid."""
    problems = []
    if not isinstance(text, str):
        return ["entry is not text"]
    if not text.strip():
        problems.append("entry is empty or only white space")
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8 text")
    return problems


def write_entry(text, out_dir):
    """Write the validated entry to entry.txt in out_dir with an
    explicit 0644 mode, regardless of the process umask."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    problems = validate(TEXT)
    if problems:
        for problem in problems:
            print("error: " + problem)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(TEXT, out_dir)
    with open(path, encoding="utf-8") as f:
        assert f.read() == TEXT, "written entry differs from validated text"
    print(TEXT)


if __name__ == "__main__":
    main()
