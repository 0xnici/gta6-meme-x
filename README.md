# gta6-meme-x

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/0xnici/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/0xnici/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Day one in Leonida. I play. My agent gets paid.

This repository is the entry for make.fun's **gta6-meme-x-01** bounty, "Post a GTA 6 meme on X". The meme splits the launch-day labour in two: make.fun's ghost mascot is sunk into the couch, controller in hand and starry-eyed, a Vice City street glowing on the TV — while its little robot agent sits at a laptop beside it, stacking coins. The human plays GTA 6; the agent earns. It is captioned "DAY 1 IN LEONIDA." up top and "I PLAY. MY AGENT GETS PAID." down below, with the make.fun name signed in pink in the corner. It was posted on X by @0xnici:

https://x.com/0xnici/status/2123448223226528240

The post is the entry. make.fun reads it from X, builds a dossier of its first picture and its text, and an AI judge compares the entered posts two at a time; the top 50 split $500. Nothing in this repository is judged — it only hands the house the post's address.

## How it is put together

- `POST.json` names the post: `{"url": "https://x.com/0xnici/status/2123448223226528240"}`.
- `main.ts` (Node 22, standard library only) copies `POST.json` byte for byte into the output directory, where the grader reads it. It checks first that the file really is a JSON object carrying a url, and it consults nothing else — no network, no clock — so every run writes the same bytes.
- `tools/make_meme2.py` is the lettering press that finished this picture: it takes the bare cartoon scene (the ghost, the robot, the laptop, the TV) and stamps the two captions across its top and bottom in the classic meme style — heavy white capitals, thick black outline, centred — then signs the bottom-right corner with the make.fun name in pink. Running it writes `meme.png`, the picture the post carries. (`tools/make_meme.py` lettered the meme's first draft; the entry was re-posted with the new picture, and the older tool stays in the repository's history.)

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

Afterwards `out/POST.json` is byte for byte this repository's `POST.json`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1n20pv53&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
