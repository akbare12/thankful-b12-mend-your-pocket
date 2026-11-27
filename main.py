import os

# Deterministic, standard-library-only entry: one fixed text, no
# randomness, no network, no clock. Writes entry.txt and nothing else.
TEXT = "Thank you for sitting with so many words today. I found the torn pocket of your coat and mended it, stitch by stitch, until the seam held. Your pen stays now. Your keys stay. The small things you carry stay. Nothing more will slip through and be lost on the floor. Rest a little now. The pocket will hold. What you carry is safe now."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
