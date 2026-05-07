#!/usr/bin/env python3
"""
Generate the exampleSite OG/Twitter card at 1200x630 px.

Renders the rail__mark logo on the left + placeholder name/tagline on the right.
Run this with --name "Your Name" --tagline "Your tagline" --domain example.com
to produce a brand-specific card. Without args you get the generic demo card.

Output: exampleSite/static/assets/og-card.png  (Hugo serves /assets/og-card.png)
"""
from __future__ import annotations

import argparse
import math
import pathlib

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG       = (10, 10, 10)
INK      = (10, 10, 10)
PAPER    = (250, 250, 247)
ACCENT   = (255, 230, 0)
MUTED    = (160, 160, 160)
HAIRLINE = (60, 60, 60)


def find_font(candidates: list[str], size: int) -> ImageFont.FreeTypeFont:
    for name in candidates:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def regular_polygon(cx: float, cy: float, r: float, sides: int, rot: float = 0) -> list[tuple[float, float]]:
    return [
        (cx + r * math.cos(rot + i * (2 * math.pi / sides)),
         cy + r * math.sin(rot + i * (2 * math.pi / sides)))
        for i in range(sides)
    ]


def draw_logo(draw: ImageDraw.ImageDraw, cx: float, cy: float, size: float) -> None:
    half = size / 2
    draw.rectangle([(cx - half, cy - half), (cx + half, cy + half)], fill=ACCENT)
    hex_pts = regular_polygon(cx, cy, size * 0.42, 6, rot=0)
    draw.polygon(hex_pts, fill=INK)
    pent_pts = regular_polygon(cx, cy, size * 0.28, 5, rot=-math.pi / 2)
    draw.polygon(pent_pts, fill=ACCENT)


def render(out: pathlib.Path, *,
           kicker: str, name_top: str, name_bot: str,
           tagline1: str, tagline2: str,
           domain: str, handle: str) -> None:
    HEADLINE = find_font([
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "DejaVuSans-Bold.ttf",
    ], 88)
    SUBLINE = find_font([
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "DejaVuSans.ttf",
    ], 32)
    MONO = find_font([
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf",
    ], 20)
    MONO_SMALL = find_font([
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
    ], 16)

    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw.rectangle([(40, 40), (W - 40, H - 40)], outline=HAIRLINE, width=1)
    draw_logo(draw, 200, H // 2, 220)

    tx = 380
    draw.text((tx, 100), kicker, font=MONO_SMALL, fill=MUTED)
    draw.text((tx, 150), name_top, font=HEADLINE, fill=PAPER)
    draw.text((tx, 245), name_bot, font=HEADLINE, fill=PAPER)
    draw.rectangle([(tx, 350), (tx + 280, 354)], fill=ACCENT)
    draw.text((tx, 380), tagline1, font=SUBLINE, fill=PAPER)
    draw.text((tx, 425), tagline2, font=SUBLINE, fill=MUTED)
    draw.text((tx, 510), domain, font=MONO, fill=ACCENT)
    if handle:
        draw.text((tx + 220, 510), f"·  {handle}", font=MONO, fill=PAPER)

    draw.rectangle([(40, H - 80), (W - 40, H - 79)], fill=HAIRLINE)
    meta = "OG · 1200 x 630"
    bb = draw.textbbox((0, 0), meta, font=MONO_SMALL)
    draw.text((W - 40 - (bb[2] - bb[0]), H - 65), meta, font=MONO_SMALL, fill=MUTED)
    draw.text((60, 55), "BRAND", font=MONO, fill=PAPER)
    draw.text((150, 55), f"/  {handle or '@yourhandle'}", font=MONO, fill=MUTED)

    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out}  ({out.stat().st_size:,} bytes)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name-top", default="Your")
    ap.add_argument("--name-bot", default="NAME")
    ap.add_argument("--kicker", default="PERSONAL · HOMEPAGE · 2026")
    ap.add_argument("--tagline1", default="What you do · One short line")
    ap.add_argument("--tagline2", default="Sub-tagline · City")
    ap.add_argument("--domain", default="example.com")
    ap.add_argument("--handle", default="@yourhandle")
    ap.add_argument("--out", default=None,
                    help="Output path. Default: <repo>/exampleSite/static/assets/og-card.png")
    args = ap.parse_args()

    out = pathlib.Path(args.out) if args.out else (
        pathlib.Path(__file__).resolve().parent.parent / "exampleSite" / "static" / "assets" / "og-card.png"
    )
    render(
        out,
        kicker=args.kicker,
        name_top=args.name_top,
        name_bot=args.name_bot,
        tagline1=args.tagline1,
        tagline2=args.tagline2,
        domain=args.domain,
        handle=args.handle,
    )


if __name__ == "__main__":
    main()
