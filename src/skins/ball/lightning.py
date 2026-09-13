import random

SKIN = {
    "name": "lightning",
    "color": (255, 255, 120),
    "trail_color": (180, 100, 255),
    "element": "lightning",
    "particle_colors": [(255, 255, 200), (255, 235, 60), (210, 140, 255), (160, 80, 255)]
}

def spawn_particles(x, y, count=8, is_trail=False):
    particles = []
    colors = SKIN["particle_colors"]
    for _ in range(count):
        particles.append({
            "x": x, "y": y,
            "vx": random.uniform(-2.8, 2.8),
            "vy": random.uniform(-2.8, 2.8),
            "life": random.randint(5, 9) if not is_trail else random.randint(4, 7),
            "max_life": 9,
            "color": random.choice(colors),
            "type": "zap",
            "size": random.choice([2, 3]) if not is_trail else 1
        })
    return particles

def update_particle(p, sim_steps):
    # Sharp erratic lightning jitter
    p["vx"] += random.uniform(-0.6, 0.6)
    p["vy"] += random.uniform(-0.6, 0.6)
