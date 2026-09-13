import random

SKIN = {
    "name": "fire",
    "color": (255, 140, 0),
    "trail_color": (255, 69, 0),
    "element": "fire",
    "particle_colors": [(255, 220, 50), (255, 140, 0), (255, 69, 0), (220, 20, 60)]
}

def spawn_particles(x, y, count=8, is_trail=False):
    particles = []
    colors = SKIN["particle_colors"]
    spd_mult = 1.0 if is_trail else 1.4
    for _ in range(count):
        particles.append({
            "x": x, "y": y,
            "vx": random.uniform(-1.6, 1.6) * spd_mult,
            "vy": (random.uniform(-3.0, -0.6) if not is_trail else random.uniform(-1.5, 0.4)),
            "life": random.randint(8, 13) if not is_trail else random.randint(5, 8),
            "max_life": 13,
            "color": random.choice(colors),
            "type": "spark" if random.random() < 0.6 else "ember",
            "size": random.choice([2, 3]) if not is_trail else 1
        })
    return particles

def update_particle(p, sim_steps):
    p["vy"] += 0.08  # Rising embers have mild gravity after initial rise
    p["vx"] *= 0.95
