import random

SKIN = {
    "name": "classic",
    "style": "classic"
}

def spawn_impact(ball_skin, hit_x, paddle_y, hit_offset):
    ball_color = ball_skin.get("color", (88, 166, 255))
    dir_x = hit_offset * 2.5
    particles = []
    for _ in range(6):
        particles.append({
            "x": hit_x + random.uniform(-3, 3),
            "y": paddle_y - random.uniform(1, 3),
            "vx": dir_x + random.uniform(-2.5, 2.5),
            "vy": random.uniform(-4.0, -1.5),
            "life": random.randint(7, 12),
            "max_life": 12,
            "color": ball_color,
            "type": "debris",
            "size": random.choice([2, 3])
        })
    return particles
