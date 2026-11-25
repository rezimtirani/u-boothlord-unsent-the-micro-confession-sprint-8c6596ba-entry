# Unsent: The Micro-Confession Sprint

[![make.fun · u-boothlord-unsent-the-micro-confession-sprint-8c6596ba](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rezimtirani/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba-entry/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rezimtirani/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba-entry/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

One micro-confession in exactly two parts: a To: line naming who it was meant for, and the unsent message itself, one line written exactly as it was typed.

> To: Mum
>
> I kept the voicemail where you said you're proud of me. I play it on the days I lie about being okay.

## How it works

`main.py` (Python 3 standard library only) writes the confession to `$MAKEFUN_OUTPUT_DIR/entry.txt`, checked first against the competition gate: UTF-8 text of 1 to 260 characters, exactly two lines, the message line at most 200 characters.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
