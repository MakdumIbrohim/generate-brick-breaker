import os
import sys
import re
import json
import urllib.request
import argparse
from datetime import datetime, timezone
from src.fetcher import fetch_contributions
from src.engine import BrickBreakerEngine
from src.gif_generator import render_gif
from src.svg_generator import render_svg
from src.config import (
    DEFAULT_SKIN, DEFAULT_THEME, DEFAULT_PADDLE_SKIN,
    BALL_SKINS, PADDLE_SKINS, THEMES, APP_VERSION
)

def parse_arguments():
    # Backward compatibility for positional CLI calls: python generate.py [user] [out] [skin] [theme] [paddle]
    # Checks if user called with flags like --skin or positional arguments
    has_flags = any(arg.startswith("-") for arg in sys.argv[1:])

    parser = argparse.ArgumentParser(
        description="Generate animated retro Brick Breaker game (SVG or GIF) from GitHub contribution graph."
    )
    parser.add_argument(
        "username",
        nargs="?",
        default=os.getenv("GITHUB_ACTOR", "MakdumIbrohim"),
        help="Target GitHub username (default: GITHUB_ACTOR env or MakdumIbrohim)"
    )

    if not has_flags and len(sys.argv) > 2:
        # Pure positional backward-compatible mode
        parser.add_argument("output", nargs="?", default="game.svg", help="Output file path (.svg or .gif)")
        parser.add_argument("skin", nargs="?", default=DEFAULT_SKIN, choices=list(BALL_SKINS.keys()), help="Ball elemental skin")
        parser.add_argument("theme", nargs="?", default=DEFAULT_THEME, choices=list(THEMES.keys()), help="Board theme")
        parser.add_argument("paddle", nargs="?", default=DEFAULT_PADDLE_SKIN, choices=list(PADDLE_SKINS.keys()), help="Paddle model skin")
        parser.add_argument("brick_color", nargs="?", default=os.getenv("BRICK_COLOR", None), help="Custom brick color HEX (1 HEX or 4 comma-separated HEX for levels 1-4, classic theme only)")
        parser.add_argument("speed", nargs="?", default=os.getenv("BALL_SPEED", None), help="Custom ball speed (slow: 4.0, normal: 6.5, fast: 9.0, turbo: 12.0, or number 2.5-20. Default: normal)")
        args = parser.parse_args()
        return args.username, args.output, args.skin, args.theme, args.paddle, args.brick_color, args.speed

    # Flag-based modern CLI mode
    parser.add_argument("-o", "--output", default="game.svg", help="Output file path (.svg or .gif)")
    parser.add_argument("-s", "--skin", default=os.getenv("BALL_SKIN", DEFAULT_SKIN), choices=list(BALL_SKINS.keys()), help="Ball elemental skin")
    parser.add_argument("-t", "--theme", default=os.getenv("THEME", DEFAULT_THEME), choices=list(THEMES.keys()), help="Board theme")
    parser.add_argument("-p", "--paddle", default=os.getenv("PADDLE_SKIN", DEFAULT_PADDLE_SKIN), choices=list(PADDLE_SKINS.keys()), help="Paddle model skin")
    parser.add_argument("-b", "--brick-color", default=os.getenv("BRICK_COLOR", None), help="Custom brick color HEX (1 HEX or 4 comma-separated HEX for levels 1-4, classic theme only)")
    parser.add_argument("--speed", default=os.getenv("BALL_SPEED", None), help="Custom ball speed: slow (4.0) | normal (6.5) | fast (9.0) | turbo (12.0), or number 2.5-20 (default: normal)")
    args = parser.parse_args()
    return args.username, args.output, args.skin, args.theme, args.paddle, args.brick_color, args.speed

def check_for_updates(token=None):
    if os.getenv("GITHUB_ACTIONS") != "true":
        return
    url = "https://api.github.com/repos/MakdumIbrohim/generate-brick-breaker/releases/latest"
    headers = {"User-Agent": "generate-brick-breaker"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            latest_tag = data.get("tag_name", "").strip()
            title = data.get("name", "").strip() or latest_tag
            pub_str = data.get("published_at", "")
            if pub_str:
                pub_date = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
                days_ago = (datetime.now(timezone.utc) - pub_date).total_seconds() / 86400
                if days_ago <= 7:
                    print(f"::notice title=What's New in {latest_tag}::{title}. See https://github.com/MakdumIbrohim/generate-brick-breaker/releases/latest")
    except Exception:
        pass

def main():
    username, output_path, skin, theme, paddle_skin, brick_color, speed = parse_arguments()
    token = os.getenv("GITHUB_TOKEN", None)

    check_for_updates(token)

    grid = fetch_contributions(username, token)
    engine = BrickBreakerEngine(grid, skin=skin, theme=theme, paddle_skin=paddle_skin, brick_color=brick_color, speed=speed)

    if output_path.lower().endswith(".svg"):
        render_svg(engine, output_path=output_path)
    else:
        render_gif(engine, output_path=output_path)

if __name__ == "__main__":
    main()
