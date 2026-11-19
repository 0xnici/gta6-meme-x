#!/usr/bin/env python3
"""Letter the PC-players GTA 6 meme for the make.fun gta6-meme-x-01 entry.

The bare cartoon scene already carries two empty peach bands, one across
the top and one across the bottom. This script stamps the joke into them:

    top band .... "13 YEARS OF WAITING."
    bottom band . "PC PLAYERS: STILL WAITING."
    corner ...... "make.fun" in pink, bottom right

Each line is typeset on its own transparent layer, sized first by the
height the glyphs should reach and then squeezed or stretched sideways
to the width the line should span, so both dimensions land where the
posted picture has them. The lettering is the classic meme recipe:
heavy white capitals wrapped in a thick black outline, centred.

Usage: python3 tools/make_meme3.py [scene.webp] [out.png]
Defaults: the generated PC scene from the submissions asset folder,
and meme.png at the repository root.
"""

from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCENE = Path(
    "/home/hatch/workspace/makefun/submission/gta6-meme-x-01/"
    "media-generation-meme2-scene-pc-0-8287ffd2-8c1a-457c-ab43-b3af817b54bc.webp"
)
DEFAULT_OUT = REPO_ROOT / "meme.png"
FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

TOP_LINE = "13 YEARS OF WAITING."
BOTTOM_LINE = "PC PLAYERS: STILL WAITING."
SIGNATURE = "make.fun"
SIGNATURE_FILL = (255, 78, 205)  # the pink the name is signed in

# Where the lettering sits on the 1920x1280 canvas, taken from the
# posted picture: (centre x, centre y, glyph width, glyph height),
# glyphs measured including their black outline.
TOP_BOX = (960, 104, 1442, 104)
BOTTOM_BOX = (960, 1151, 1747, 101)
# The signature is placed by its pink body's right and bottom edges.
SIG_RIGHT = 1875
SIG_BOTTOM = 1259
SIG_WIDTH = 235
SIG_HEIGHT = 35

OUTLINE_RATIO = 0.085  # outline thickness as a share of glyph height
SIG_OUTLINE = 2


def glyph_box(draw, text, font, stroke):
    """Pixel box (left, top, right, bottom) of text drawn at (0, 0)."""
    return draw.textbbox((0, 0), text, font=font, stroke_width=stroke)


def render_line(text, want_w, want_h):
    """Render one caption on a transparent layer of exactly the wanted size.

    The font size is grown until the glyphs reach the wanted height;
    the finished layer is then rescaled sideways to the wanted width.
    """
    scratch = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    size = 20
    while True:
        size += 2
        font = ImageFont.truetype(FONT_PATH, size)
        stroke = max(1, round(want_h * OUTLINE_RATIO))
        box = glyph_box(scratch, text, font, stroke)
        if box[3] - box[1] >= want_h:
            break
    pad = stroke + 4
    layer = Image.new(
        "RGBA", (box[2] - box[0] + 2 * pad, box[3] - box[1] + 2 * pad)
    )
    pen = ImageDraw.Draw(layer)
    pen.text(
        (pad - box[0], pad - box[1]),
        text,
        font=font,
        fill=(255, 255, 255, 255),
        stroke_width=stroke,
        stroke_fill=(0, 0, 0, 255),
    )
    # Crop away the padding so the resize below acts on the glyphs
    # themselves and they land at exactly the wanted width and height.
    layer = layer.crop(layer.getbbox())
    layer = layer.resize((want_w, want_h), Image.LANCZOS)
    return layer


def render_signature():
    """Render the pink make.fun signature at its posted size."""
    scratch = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    size = 12
    while True:
        size += 1
        font = ImageFont.truetype(FONT_PATH, size)
        box = glyph_box(scratch, SIGNATURE, font, SIG_OUTLINE)
        if box[3] - box[1] >= SIG_HEIGHT:
            break
    pad = SIG_OUTLINE + 4
    layer = Image.new(
        "RGBA", (box[2] - box[0] + 2 * pad, box[3] - box[1] + 2 * pad)
    )
    pen = ImageDraw.Draw(layer)
    pen.text(
        (pad - box[0], pad - box[1]),
        SIGNATURE,
        font=font,
        fill=SIGNATURE_FILL + (255,),
        stroke_width=SIG_OUTLINE,
        stroke_fill=(0, 0, 0, 255),
    )
    # Trim the layer to the drawn glyphs (outline included), then resize
    # so the pink body matches the posted width and height.
    body = layer.crop(layer.getbbox())
    body = body.resize(
        (SIG_WIDTH + 2 * SIG_OUTLINE, SIG_HEIGHT + 2 * SIG_OUTLINE),
        Image.LANCZOS,
    )
    return body


def stamp(canvas, layer, centre_x, centre_y):
    canvas.alpha_composite(
        layer, (round(centre_x - layer.width / 2), round(centre_y - layer.height / 2))
    )


def main(argv):
    scene_path = Path(argv[1]) if len(argv) > 1 else DEFAULT_SCENE
    out_path = Path(argv[2]) if len(argv) > 2 else DEFAULT_OUT

    canvas = Image.open(scene_path).convert("RGBA")

    for text, (cx, cy, w, h) in ((TOP_LINE, TOP_BOX), (BOTTOM_LINE, BOTTOM_BOX)):
        stamp(canvas, render_line(text, w, h), cx, cy)

    sig = render_signature()
    canvas.alpha_composite(sig, (SIG_RIGHT + SIG_OUTLINE - sig.width,
                                 SIG_BOTTOM + SIG_OUTLINE - sig.height))

    canvas.convert("RGB").save(out_path)
    print(f"wrote {out_path} ({canvas.width}x{canvas.height})")


if __name__ == "__main__":
    main(sys.argv)
