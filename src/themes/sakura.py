import math
import random

THEME = {
    "name": "sakura",
    "bg_effect": "sakura_drift",
    "bg_color": (26, 16, 47),          # Midnight spring pastel twilight
    "paddle_color": (255, 83, 118),     # Vibrant lotus blossom pink
    "empty_brick": (42, 28, 74),        # Dark twilight purple empty cells
    "heart_color": (255, 64, 129),      # Vivid cherry blossom heart
    "score_text_color": (254, 223, 225),# Soft sakura white-pink text
    "banner_bg_color": (38, 24, 66),
    "win_text_color": (168, 216, 185),  # Fresh spring leaf green
    "lose_text_color": (255, 110, 140),
    "brick_colors": [
        (140, 70, 120),  # 1-2 commits (plum blossom purple)
        (200, 100, 150), # 3-5 commits (deep rose pink)
        (244, 167, 185), # 6-9 commits (fresh cherry petal)
        (255, 195, 215)  # 10+ commits (luminous pale sakura)
    ]
}

def init_ambient(canvas_w, canvas_h):
    petals = []
    # 20 floating sakura petals
    for _ in range(20):
        petals.append({
            "type": "petal",
            "x": random.uniform(-20, canvas_w + 20),
            "y": random.uniform(0, canvas_h),
            "vx": random.uniform(0.3, 0.8),
            "vy": random.uniform(0.4, 0.9),
            "w": random.uniform(5, 8),
            "h": random.uniform(3, 5),
            "angle": random.uniform(0, 360),
            "spin_spd": random.uniform(0.04, 0.1)
        })
    return petals

def update_ambient(items, sim_steps, canvas_w, canvas_h):
    for p in items:
        p["x"] += p["vx"] + math.sin(sim_steps * 0.08 + p["y"]) * 0.35
        p["y"] += p["vy"]
        p["angle"] += p["spin_spd"]

        # Loop back from top-left if it drifts out of canvas
        if p["y"] > canvas_h + 10 or p["x"] > canvas_w + 20:
            p["y"] = -10
            p["x"] = random.uniform(-20, canvas_w - 40)
