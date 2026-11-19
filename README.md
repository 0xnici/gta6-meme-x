# gta6-meme-x

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/0xnici/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/0xnici/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Thirteen years of waiting — and PC players are still waiting.

This repository is the entry for make.fun's **gta6-meme-x-01** bounty, "Post a GTA 6 meme on X". The picture is a small tragedy in one frame: make.fun's ghost mascot sits at its desk in tears, controller in hand, while its gaming PC stands beside it furred with dust and cobwebs — a shrine to a port that never came. The monitor taunts it with a Vice City sunset everyone else gets to play in, and the laptop open on make.fun is the only machine in the room still earning its keep. "13 YEARS OF WAITING." runs across the top and "PC PLAYERS: STILL WAITING." across the bottom, with the make.fun name signed in pink in the bottom-right corner. It was posted on X by @0xnici:

https://x.com/0xnici/status/2123448223226528240

The post is the entry. make.fun reads it from X, builds a dossier of its first picture and its text, and an AI judge compares the entered posts two at a time; the top 50 split $500. Nothing in this repository is judged — it only hands the house the post's address.

## How it is put together

- `POST.json` names the post: `{"url": "https://x.com/0xnici/status/2123448223226528240"}`.
- `main.ts` (Node 22, standard library only) copies `POST.json` byte for byte into the output directory, where the grader reads it. It checks first that the file really is a JSON object carrying a url, and it consults nothing else — no network, no clock — so every run writes the same bytes.
- `tools/make_meme3.py` is the lettering press that finished this picture: it takes the bare cartoon scene (the tearful ghost, the cobwebbed PC, the monitor, the laptop) and stamps the two captions into its empty top and bottom bands in the classic meme style — heavy white capitals, thick black outline, centred — then signs the bottom-right corner with the make.fun name in pink. Running it writes `meme.png`, the picture the post carries. (Earlier drafts of the entry were lettered by `tools/make_meme.py` and `tools/make_meme2.py`; those tools stay in the repository, but this is the picture that was finally posted.)

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

Afterwards `out/POST.json` is byte for byte this repository's `POST.json`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1n20pv53&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
