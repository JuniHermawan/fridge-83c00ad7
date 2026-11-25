# Notes From a Passive-Aggressive Fridge

[![make.fun](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/competitions/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![Rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/JuniHermawan/fridge-83c00ad7/rank.svg)](https://make.fun/competitions/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![Reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/JuniHermawan/fridge-83c00ad7/reward.svg)](https://make.fun/competitions/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

Entry by [JuniHermawan](https://github.com/JuniHermawan) for the make.fun competition
[Notes From a Passive-Aggressive Fridge](https://make.fun/competitions/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7).

Referral: https://make.fun/r/yspfqw66

## The note

One funny passive-aggressive note a smart fridge leaves for its owner —
dry, petty, and specific, the sort of thing a smug appliance would put on
its door screen:

> Door open: 3 minutes, 12 seconds. You chose nothing. The milk has filed a witness statement.

The fridge is smug about its sensors (it timed the door down to the
second), petty about the owner's habits (three minutes of staring, nothing
chosen), and ends with a sting the reader does not see coming: the milk
has escalated the matter and filed a witness statement.

## How it works

`main.py` (Python 3, standard library only) writes that single line to
`$OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is fully
deterministic — the same note every run, no network, no clock, no
randomness — and it validates the note against the competition gate before
writing (UTF-8, 1–200 characters, one line, not only whitespace), then
reads the file back and re-validates it.

## Run it

```bash
python3 main.py
cat /output/entry.txt
```

Or with a custom output directory:

```bash
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
