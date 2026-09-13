import random

SKIN = {
    "name": "cyber",
    "style": "cyber",
    "primary": (210, 80, 255),
    "core": (0, 255, 200),
    "caps": (120, 20, 200)
}

def spawn_impact(ball_skin, hit_x, paddle_y, hit_offset):
    dir_x = hit_offset * 2.5
    particles = []
    for _ in range(7):
        particles.append({
            "x": hit_x + random.uniform(-4, 4),
            "y": paddle_y - random.uniform(2, 4),
            "vx": dir_x + random.uniform(-3.0, 3.0),
            "vy": random.uniform(-4.8, -1.6),
            "life": random.randint(8, 14),
            "max_life": 14,
            "color": random.choice([(210, 80, 255), (0, 255, 200), (255, 255, 255)]),
            "type": "pixel",
            "size": random.choice([3, 4])
        })
    return particles
