THEME = {
    "name": "sky",
    "bg_effect": "mario_sky",
    "bg_color": (107, 140, 255),
    "paddle_color": (230, 75, 50),
    "empty_brick": (140, 168, 255),
    "heart_color": (255, 60, 60),
    "score_text_color": (255, 255, 255),
    "banner_bg_color": (255, 255, 255),
    "win_text_color": (34, 139, 34),
    "lose_text_color": (207, 34, 46),
    "brick_colors": [
        (255, 200, 110),
        (240, 150, 40),
        (195, 90, 20),
        (145, 50, 10)
    ]
}

def init_ambient(canvas_w, canvas_h):
    return [
        {"type": "cloud", "x": 30, "y": 140, "speed": 0.24, "scale": 1.1},
        {"type": "cloud", "x": 260, "y": 185, "speed": 0.18, "scale": 0.85},
        {"type": "cloud", "x": 480, "y": 148, "speed": 0.22, "scale": 1.25},
        {"type": "cloud", "x": -70, "y": 170, "speed": 0.20, "scale": 0.95},
        {"type": "bird", "x": 120, "y": 135, "speed": 0.55, "scale": 1.0},
        {"type": "bird", "x": -40, "y": 155, "speed": 0.48, "scale": 0.85}
    ]

def update_ambient(items, sim_steps, canvas_w, canvas_h):
    for it in items:
        it["x"] += it["speed"]
        if it["type"] == "cloud" and it["x"] > canvas_w + 50:
            it["x"] = -110
        elif it["type"] == "bird" and it["x"] > canvas_w + 30:
            it["x"] = -60
