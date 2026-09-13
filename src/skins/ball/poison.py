import math
import random

SKIN = {
    "name": "poison",
    "color": (57, 211, 83),
    "trail_color": (35, 134, 54),
    "element": "poison",
    "particle_colors": [(126, 231, 135), (57, 211, 83), (35, 134, 54), (0, 109, 50)]
}

def spawn_particles(x, y, count=8, is_trail=False):
    particles = []
    colors = SKIN["particle_colors"]
    spd_mult = 1.0 if is_trail else 1.4
    for _ in range(count):
        particles.append({
            "x": x, "y": y,
            "vx": random.uniform(-1.4, 1.4) * spd_mult,
            "vy": random.uniform(-2.5, 0.5) if not is_trail else random.uniform(-1.6, -0.3),
            "life": random.randint(9, 15) if not is_trail else random.randint(6, 10),
            "max_life": 15,
            "color": random.choice(colors),
            "type": "bubble",
            "size": random.choice([2, 3]) if not is_trail else 2
        })
    return particles

def update_particle(p, sim_steps):
    # Wafting upward toxic bubble motion
    p["x"] += math.cos(sim_steps * 0.15) * 0.3
