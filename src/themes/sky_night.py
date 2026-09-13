import math
import random

THEME = {
    "name": "sky-night",
    "bg_effect": "mario_sky_night",
    "bg_color": (13, 27, 62),         # Deep midnight blue
    "paddle_color": (255, 180, 80),     # Warm lantern amber
    "empty_brick": (24, 42, 88),       # Dark translucent night cells
    "heart_color": (255, 75, 90),
    "score_text_color": (220, 235, 255),
    "banner_bg_color": (20, 36, 76),
    "win_text_color": (120, 230, 150),
    "lose_text_color": (255, 90, 100),
    "brick_colors": [
        (80, 120, 190),  # 1-2 commits (moonlit slate blue)
        (110, 160, 230), # 3-5 commits (bright twilight blue)
        (180, 150, 240), # 6-9 commits (mystic night purple)
        (255, 215, 120)  # 10+ commits (glowing star gold)
    ]
}

def init_ambient(canvas_w, canvas_h):
    items = []
    # Twinkling night stars
    for _ in range(25):
        items.append({
            "type": "star",
            "x": random.uniform(5, canvas_w - 5),
            "y": random.uniform(5, canvas_h - 20),
            "brightness": random.uniform(0.2, 1.0),
            "speed": random.uniform(0.02, 0.05),
            "size": 1 if random.random() < 0.8 else 2
        })
    # Dim, translucent night clouds
    night_clouds = [
        {"type": "cloud", "x": 40, "y": 145, "speed": 0.18, "scale": 1.1},
        {"type": "cloud", "x": 280, "y": 182, "speed": 0.14, "scale": 0.85},
        {"type": "cloud", "x": 490, "y": 152, "speed": 0.16, "scale": 1.2},
        {"type": "cloud", "x": -60, "y": 172, "speed": 0.15, "scale": 0.95}
    ]
    items.extend(night_clouds)
    # Floating retro Boo ghost drifting through the night
    items.append({"type": "ghost", "x": 110, "y": 138, "speed": 0.42, "scale": 1.0})
    items.append({"type": "ghost", "x": -50, "y": 164, "speed": 0.36, "scale": 0.85})
    return items

def update_ambient(items, sim_steps, canvas_w, canvas_h):
    for it in items:
        if it["type"] == "star":
            it["brightness"] = (math.sin(sim_steps * it["speed"] + it["x"]) + 1) / 2
        elif it["type"] == "cloud":
            it["x"] += it["speed"]
            if it["x"] > canvas_w + 50:
                it["x"] = -110
        elif it["type"] == "ghost":
            it["x"] += it["speed"]
            if it["x"] > canvas_w + 40:
                it["x"] = -60
