import random

SKIN = {
    "name": "mecha",
    "style": "mecha",
    "primary": (139, 148, 158),
    "plate": (240, 246, 252),
    "booster": (255, 75, 75)
}

def spawn_impact(ball_skin, hit_x, paddle_y, hit_offset):
    dir_x = hit_offset * 2.5
    particles = []
    for _ in range(8):
        particles.append({
            "x": hit_x + random.uniform(-4, 4),
            "y": paddle_y - random.uniform(1, 4),
            "vx": dir_x + random.uniform(-2.5, 2.5),
            "vy": random.uniform(-4.5, -1.8),
            "life": random.randint(8, 14),
            "max_life": 14,
            "color": random.choice([(255, 60, 20), (255, 140, 0), (255, 240, 60)]),
            "type": "thrust",
            "size": random.choice([3, 4])
        })
    return particles
