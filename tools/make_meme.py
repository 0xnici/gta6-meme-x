#!/usr/bin/env python3
"""Build the GTA 6 meme for the make.fun gta6-meme-x-01 entry.

The artwork is a finished cartoon scene (two make.fun ghosts on a couch,
controllers in hand, a Vice City street glowing on the TV) that already
carries a plain peach band across its top and bottom edges. This script
letters the two bands in the classic meme style -- heavy white capitals
with a thick black outline, centred -- and signs the bottom-right corner
with the make.fun name in magenta.

Usage:
    python3 tools/make_meme.py [scene.png] [output.png]

With no arguments it reads the scene from the entry's asset folder and
writes meme.png at the repository root.
"""

from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCENE = Path(
    "/home/hatch/workspace/makefun/submission/gta6-meme-x-01/"
    "media-generation-meme-scene-0-d9c31a2c-fa88-42af-8662-6a339de67d22.png"
)
DEFAULT_OUTPUT = REPO_ROOT / "meme.png"

FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

HEADLINE = "13 YEARS OF WAITING."
PUNCHLINE = "THE WHOLE OFFICE CALLED IN SICK."
SIGNATURE = "make.fun"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAGENTA = (255, 78, 205)  # #ff4ecd


def load_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size)


def text_width(draw: ImageDraw.ImageDraw, text: str, font, stroke: int) -> float:
    """Rendered width of a string, outline included."""
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke)
    return box[2] - box[0]


def shrink_to_fit(draw, text: str, max_width: float, start_size: int):
    """Largest font size, stepping down from start_size, whose stroked
    rendering of text stays within max_width. Returns (font, stroke)."""
    size = start_size
    while size > 8:
        font = load_font(size)
        stroke = max(2, round(size / 13))
        if text_width(draw, text, font, stroke) <= max_width:
            return font, stroke
        size -= 2
    font = load_font(size)
    return font, max(2, round(size / 13))


def draw_centred(draw, text: str, centre_y: float, font, stroke: int, fill, canvas_width: int) -> None:
    """Draw one line of text centred horizontally on the canvas, with the
    middle of the glyphs sitting on centre_y."""
    width = text_width(draw, text, font, stroke)
    x = (canvas_width - width) / 2
    # textbbox gives the glyph box for a (0, 0) anchor; shift so its centre
    # lands on centre_y instead of its top.
    top, bottom = draw.textbbox((0, 0), text, font=font, stroke_width=stroke)[1::2]
    y = centre_y - (top + bottom) / 2
    draw.text((x, y), text, font=font, fill=fill, stroke_width=stroke, stroke_fill=BLACK)


def build(scene_path: Path, output_path: Path) -> None:
    canvas = Image.open(scene_path).convert("RGB")
    width, height = canvas.size
    draw = ImageDraw.Draw(canvas)

    # Headline in the top band, punchline in the bottom band. Each line is
    # fitted to its own width allowance -- the short headline letters
    # larger and narrower, the long punchline smaller and wider -- and
    # centred in its band.
    head_font, head_stroke = shrink_to_fit(
        draw, HEADLINE, max_width=width * 0.725, start_size=round(height * 0.14)
    )
    draw_centred(draw, HEADLINE, height * 0.088, head_font, head_stroke, WHITE, width)

    punch_font, punch_stroke = shrink_to_fit(
        draw, PUNCHLINE, max_width=width * 0.90, start_size=round(height * 0.14)
    )
    draw_centred(draw, PUNCHLINE, height * 0.888, punch_font, punch_stroke, WHITE, width)

    # The signature: small, magenta, tucked into the bottom-right corner
    # below the punchline, with a hairline outline to hold it off the peach.
    sign_font, sign_stroke = shrink_to_fit(
        draw, SIGNATURE, max_width=width * 0.133, start_size=round(height * 0.05)
    )
    sign_box = draw.textbbox((0, 0), SIGNATURE, font=sign_font, stroke_width=sign_stroke)
    sign_x = width * 0.98 - sign_box[2]
    sign_y = height * 0.99 - sign_box[3]
    draw.text(
        (sign_x, sign_y),
        SIGNATURE,
        font=sign_font,
        fill=MAGENTA,
        stroke_width=sign_stroke,
        stroke_fill=BLACK,
    )

    canvas.save(output_path)
    print(f"wrote {output_path} ({width}x{height})")


if __name__ == "__main__":
    scene = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SCENE
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT
    build(scene, output)
