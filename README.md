# tiny-chess-v3b

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Man899/tiny-chess-v3b/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Man899/tiny-chess-v3b/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 0x88 alpha-beta chess engine: 100k nodes/move, null-move pruning, quiescence, LMR and a transposition table. Mean Elo 1,430 across three practice trials (1,497 / 1,430 / 1,362) vs the sunfish-4k baseline mean of 1,360. Built for speed first: same strength class as v3 with far more timing headroom (worst trial wall 2,449 s vs 3,241 s, worst move 4.16 s vs 6.46 s). `main.py` loads the lzma-packed engine from `engine.lzma`.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=5e0gj8t6&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
