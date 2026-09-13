import math
import random

THEME = {
    "name": "classic",
    "bg_effect": "starfield",
    "bg_color": None,                 # Transparent background (adapts natively to GitHub Dark/Light)
    "paddle_color": (88, 166, 255),
    "empty_brick": (22, 27, 34),
    "heart_color": (255, 107, 107),
    "score_text_color": (139, 148, 158),
    "banner_bg_color": (22, 27, 34),
    "win_text_color": (57, 211, 83),
    "lose_text_color": (248, 81, 73),
    "brick_colors": [
        (14, 68, 41),
        (0, 109, 50),
        (38, 166, 65),
        (57, 211, 83)
    ]
}

def init_ambient(canvas_w, canvas_h):
    items = []
    for _ in range(35):
        items.append({
            "x": random.uniform(5, canvas_w - 5),
            "y": random.uniform(5, canvas_h - 10),
            "brightness": random.uniform(0.2, 1.0),
            "speed": random.uniform(0.02, 0.06),
            "size": 1 if random.random() < 0.8 else 2
        })
    return items

def update_ambient(items, sim_steps, canvas_w, canvas_h):
    for s in items:
        s["brightness"] = (math.sin(sim_steps * s["speed"] + s["x"]) + 1) / 2
