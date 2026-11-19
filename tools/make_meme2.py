#!/usr/bin/env python3
"""Lettering press for the second gta6-meme-x-01 meme ("my agent gets paid").

Takes the bare cartoon scene -- a make.fun ghost on a couch, controller in
hand, its little robot agent at a laptop beside it, a Vice City street
glowing on the TV -- and finishes it as a classic meme: one bold white
caption across the top, one across the bottom, both in heavy capitals with
a thick black outline, and the make.fun name signed in pink in the
bottom-right corner.

Usage:
    python3 tools/make_meme2.py [scene.webp] [output.png]

With no arguments it reads the scene from the submission assets folder and
writes meme.png at the repository root.
"""

from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCENE = (
    "/home/hatch/workspace/makefun/submission/gta6-meme-x-01/"
    "media-generation-meme2-scene-agent-0-246cd754-e9de-43bb-86e2-e6919307fb3e.webp"
)
DEFAULT_OUT = REPO_ROOT / "meme.png"
FONT_FILE = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

HEADLINE = "DAY 1 IN LEONIDA."
PUNCHLINE = "I PLAY. MY AGENT GETS PAID."
SIGNATURE = "make.fun"
SIGNATURE_PINK = (252, 77, 202)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def ink_box(draw, text, font, stroke):
    """Bounding box (x0, y0, x1, y1) of the ink `text` would leave."""
    return draw.textbbox((0, 0), text, font=font, stroke_width=stroke)


def font_for_width(draw, text, want_width, stroke_ratio=11):
    """Largest bold font whose ink for `text` is at most `want_width` wide."""
    size = 16
    best = ImageFont.truetype(FONT_FILE, size)
    while size <= 600:
        font = ImageFont.truetype(FONT_FILE, size)
        stroke = max(2, size // stroke_ratio)
        x0, _, x1, _ = ink_box(draw, text, font, stroke)
        if x1 - x0 > want_width:
            break
        best = font
        size += 2
    return best


def stamp(draw, text, font, centre_x, ink_top, fill, stroke):
    """Draw `text` centred on `centre_x` with its ink starting at `ink_top`."""
    x0, y0, x1, _ = ink_box(draw, text, font, stroke)
    draw.text(
        (centre_x - (x0 + x1) // 2, ink_top - y0),
        text,
        font=font,
        fill=fill,
        stroke_width=stroke,
        stroke_fill=BLACK,
    )


def letter(scene_path, out_path):
    img = Image.open(scene_path).convert("RGB")
    width, height = img.size
    draw = ImageDraw.Draw(img)
    mid = width // 2

    # Headline: ink begins a short way below the top edge and spans about
    # three fifths of the width, centred.
    head_font = font_for_width(draw, HEADLINE, int(width * 0.615))
    stamp(
        draw,
        HEADLINE,
        head_font,
        mid,
        int(height * 0.041),
        WHITE,
        max(2, head_font.size // 11),
    )

    # Punchline: nearly the full width of the frame, ink sitting just above
    # the bottom edge.
    punch_font = font_for_width(draw, PUNCHLINE, int(width * 0.935))
    stamp(
        draw,
        PUNCHLINE,
        punch_font,
        mid,
        int(height * 0.860),
        WHITE,
        max(2, punch_font.size // 11),
    )

    # Signature: small pink bold in the bottom-right corner, its ink ending
    # a short margin in from the right and bottom edges.
    sig_font = font_for_width(draw, SIGNATURE, int(width * 0.130))
    sig_stroke = 2
    x0, y0, x1, y1 = ink_box(draw, SIGNATURE, sig_font, sig_stroke)
    draw.text(
        (width - int(width * 0.023) - x1, height - int(height * 0.016) - y1),
        SIGNATURE,
        font=sig_font,
        fill=SIGNATURE_PINK,
        stroke_width=sig_stroke,
        stroke_fill=BLACK,
    )

    img.save(out_path)
    print(f"wrote {out_path} ({width}x{height})")


if __name__ == "__main__":
    scene = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SCENE
    out = sys.argv[2] if len(sys.argv) > 2 else str(DEFAULT_OUT)
    letter(scene, out)
