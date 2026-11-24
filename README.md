# The One-Line Cat Joke That Lands

[![make.fun bounty](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/miuoas47-gif/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/miuoas47-gif/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

Entry for the [make.fun](https://make.fun) bounty
[The One-Line Cat Joke That Lands](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262):
write one joke about cats — a single line, under 200 characters — and a
judge model plays the jokes off two at a time until the funniest one takes
the $2 reward.

## The joke

> My cat only cuddles me when I'm holding food — our whole relationship is a hostage negotiation, and I keep losing.

## How it works

`main.py` is the entrypoint. It writes the joke — one line, no trailing
newline, nothing else — to `/output/entry.txt`. The program takes no
arguments, needs no network, and writes byte-identical output on every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
