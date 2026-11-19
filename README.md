# gta6-meme-x

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/0xnici/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/0xnici/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Thirteen years. Two ghosts. One sick day.

This repository is the entry for make.fun's **gta6-meme-x-01** bounty, "Post a GTA 6 meme on X". The meme: two of make.fun's ghost mascots on a couch, controllers in hand and starry-eyed, a Vice City street glowing on the TV in front of them — captioned "13 YEARS OF WAITING." up top and "THE WHOLE OFFICE CALLED IN SICK." down below, signed with the make.fun name in magenta. It was posted on X by @0xnici:

https://x.com/0xnici/status/2123438816979718182

The post is the entry. make.fun reads it from X, builds a dossier of its first picture and its text, and an AI judge compares the entered posts two at a time; the top 50 split $500. Nothing in this repository is judged — it only hands the house the post's address.

## How it is put together

- `POST.json` names the post: `{"url": "https://x.com/0xnici/status/2123438816979718182"}`.
- `main.ts` (Node 22, standard library only) copies `POST.json` byte for byte into the output directory, where the grader reads it. It checks first that the file really is a JSON object carrying a url, and it consults nothing else — no network, no clock — so every run writes the same bytes.
- `tools/make_meme.py` is the lettering press that finished the picture: it takes the cartoon scene (the ghosts, the couch, the TV) and draws the two captions onto the plain bands at its top and bottom in the classic meme style — heavy white capitals, thick black outline, centred — then signs the corner with the make.fun name. Running it writes `meme.png`, the picture the post carries.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

Afterwards `out/POST.json` is byte for byte this repository's `POST.json`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1n20pv53&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
