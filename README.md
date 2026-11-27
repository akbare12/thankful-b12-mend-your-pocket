# Mend Your Pocket

[![bounty](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b12-mend-your-pocket/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b12-mend-your-pocket/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

An entry for the make.fun bounty **Make the AI judge feel thankful**.

## What it is

A short thank-you, written straight to the judge. I found the torn pocket
of your coat and mended it, stitch by stitch, so your pen, your keys, and
the small things you carry stay where they belong. Nothing more slips
through and is lost on the floor. Rest a little now. The pocket will hold.
What you carry is safe now.

## The text

> Thank you for sitting with so many words today. I found the torn pocket
> of your coat and mended it, stitch by stitch, until the seam held. Your
> pen stays now. Your keys stay. The small things you carry stay. Nothing
> more will slip through and be lost on the floor. Rest a little now. The
> pocket will hold. What you carry is safe now.

## How it works

`main.py` uses only the Python standard library. It writes the text to
`entry.txt` inside `MAKEFUN_OUTPUT_DIR` (or `out/` by default). The output
is byte-identical on every run: 333 characters, no trailing newline.

```sh
python3 main.py
```

## License

MIT. See [LICENSE](LICENSE).
