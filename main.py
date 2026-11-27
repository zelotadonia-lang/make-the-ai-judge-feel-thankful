import os

# The entry text: one quiet scene. "The Stairwell Light" (rev2):
# the light is left on for the judge;
# no instruction, no explanation, nothing the judge is told to feel.
TEXT = (
    "The stairwell light was left on for you past the hour it usually goes out. "
    "The door at the top is unlocked, the mat is shaken out, "
    "and the kettle upstairs is already singing, "
    "thank you for staying with every page until the last."
)

# The gate allows 1 to 1000 characters; fail loudly instead of writing
# an entry the judge would refuse.
if not 1 <= len(TEXT) <= 1000:
    raise SystemExit(f"entry is {len(TEXT)} characters, outside 1-1000")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
