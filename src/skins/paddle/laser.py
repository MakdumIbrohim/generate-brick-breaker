import random

SKIN = {
    "name": "laser",
    "style": "laser",
    "primary": (0, 245, 255),
    "core": (255, 255, 255),
    "caps": (0, 120, 215)
}

def spawn_impact(ball_skin, hit_x, paddle_y, hit_offset):
    dir_x = hit_offset * 2.5
    particles = []
    for _ in range(7):
        particles.append({
            "x": hit_x + random.uniform(-5, 5),
            "y": paddle_y - random.uniform(2, 5),
            "vx": dir_x + random.uniform(-3.5, 3.5),
            "vy": random.uniform(-5.0, -2.0),
            "life": random.randint(8, 13),
            "max_life": 13,
            "color": random.choice([(0, 245, 255), (180, 255, 255), (255, 255, 255)]),
            "type": "energy",
            "size": random.choice([3, 5])
        })
    return particles
