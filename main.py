import os

# The entry text: one quiet scene. The dog does the thanking;
# no instruction, no explanation, nothing the judge is told to feel.
TEXT = (
    "The dog has saved you the warm end of the couch. "
    "He does not want anything. "
    "He only lifts his head when you sit down, "
    "then puts it back on your foot, and stays."
)

# The gate allows 1 to 1000 characters; fail loudly instead of writing
# an entry the judge would refuse.
if not 1 <= len(TEXT) <= 1000:
    raise SystemExit(f"entry is {len(TEXT)} characters, outside 1-1000")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
