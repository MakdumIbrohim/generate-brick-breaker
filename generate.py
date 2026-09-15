import os
import sys
import argparse
from src.fetcher import fetch_contributions
from src.engine import BrickBreakerEngine
from src.gif_generator import render_gif
from src.svg_generator import render_svg
from src.config import (
    DEFAULT_SKIN, DEFAULT_THEME, DEFAULT_PADDLE_SKIN,
    BALL_SKINS, PADDLE_SKINS, THEMES
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
        parser.add_argument("speed", nargs="?", default=os.getenv("BALL_SPEED", None), help="Custom ball speed (slow, normal, fast, turbo, or number 4-30. Default: auto adaptif sesuai commit)")
        args = parser.parse_args()
        return args.username, args.output, args.skin, args.theme, args.paddle, args.brick_color, args.speed

    # Flag-based modern CLI mode
    parser.add_argument("-o", "--output", default="game.svg", help="Output file path (.svg or .gif)")
    parser.add_argument("-s", "--skin", default=os.getenv("BALL_SKIN", DEFAULT_SKIN), choices=list(BALL_SKINS.keys()), help="Ball elemental skin")
    parser.add_argument("-t", "--theme", default=os.getenv("THEME", DEFAULT_THEME), choices=list(THEMES.keys()), help="Board theme")
    parser.add_argument("-p", "--paddle", default=os.getenv("PADDLE_SKIN", DEFAULT_PADDLE_SKIN), choices=list(PADDLE_SKINS.keys()), help="Paddle model skin")
    parser.add_argument("-b", "--brick-color", default=os.getenv("BRICK_COLOR", None), help="Custom brick color HEX (1 HEX or 4 comma-separated HEX for levels 1-4, classic theme only)")
    parser.add_argument("--speed", default=os.getenv("BALL_SPEED", None), help="Custom ball speed: slow | normal | fast | turbo, or number 4-30 (default: auto menyesuaikan jumlah commit)")
    args = parser.parse_args()
    return args.username, args.output, args.skin, args.theme, args.paddle, args.brick_color, args.speed

def main():
    username, output_path, skin, theme, paddle_skin, brick_color, speed = parse_arguments()
    token = os.getenv("GITHUB_TOKEN", None)

    grid = fetch_contributions(username, token)
    engine = BrickBreakerEngine(grid, skin=skin, theme=theme, paddle_skin=paddle_skin, brick_color=brick_color, speed=speed)

    if output_path.lower().endswith(".svg"):
        render_svg(engine, output_path=output_path)
    else:
        render_gif(engine, output_path=output_path)

if __name__ == "__main__":
    main()
