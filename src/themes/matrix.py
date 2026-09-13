import random

THEME = {
    "name": "matrix",
    "bg_effect": "matrix_rain",
    "bg_color": (5, 15, 8),
    "paddle_color": (0, 255, 70),
    "empty_brick": (12, 30, 16),
    "heart_color": (0, 255, 120),
    "score_text_color": (80, 180, 100),
    "banner_bg_color": (10, 28, 15),
    "win_text_color": (0, 255, 70),
    "lose_text_color": (255, 70, 70),
    "brick_colors": [
        (0, 60, 20),
        (0, 120, 40),
        (0, 190, 60),
        (0, 255, 70)
    ]
}

def init_ambient(canvas_w, canvas_h):
    items = []
    cols = int(canvas_w / 16)
    for c in range(cols):
        items.append({
            "x": c * 16 + 8,
            "y": random.uniform(0, canvas_h),
            "speed": random.uniform(1.2, 2.5),
            "len": random.randint(4, 9)
        })
    return items

def update_ambient(items, sim_steps, canvas_w, canvas_h):
    for col in items:
        col["y"] += col["speed"]
        if col["y"] > canvas_h + 30:
            col["y"] = -random.uniform(10, 40)
