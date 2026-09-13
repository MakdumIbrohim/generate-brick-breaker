import random

SKIN = {
    "name": "retro",
    "style": "retro",
    "primary": (235, 130, 60),
    "stripes": (255, 215, 0),
    "caps": (160, 60, 20)
}

def spawn_impact(ball_skin, hit_x, paddle_y, hit_offset):
    dir_x = hit_offset * 2.5
    particles = []
    for _ in range(8):
        particles.append({
            "x": hit_x + random.uniform(-4, 4),
            "y": paddle_y - random.uniform(1, 4),
            "vx": dir_x + random.uniform(-2.8, 2.8),
            "vy": random.uniform(-4.5, -1.5),
            "life": random.randint(9, 15),
            "max_life": 15,
            "color": random.choice([(255, 215, 0), (255, 245, 160), (255, 140, 0)]),
            "type": "pixel",
            "size": random.choice([3, 5])
        })
    return particles
