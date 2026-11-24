# The One-Line AI Excuse for Breaking Production

Entry for the make.fun bounty: https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66

[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/freysiatiara/ai-excuse-breaking-production-20261124/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/freysiatiara/ai-excuse-breaking-production-20261124/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

## The line

> Sorry — I read "deploy to staging" as "stage a coup against the database", and the database has officially surrendered.

## How it works

`main.py` (Python stdlib only) writes exactly that one line — no trailing
newline, 119 characters — to `/output/entry.txt` and sets the file mode to
0644.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
