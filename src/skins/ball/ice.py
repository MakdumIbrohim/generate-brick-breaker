import math
import random

SKIN = {
    "name": "ice",
    "color": (175, 238, 255),
    "trail_color": (88, 166, 255),
    "element": "ice",
    "particle_colors": [(240, 250, 255), (175, 238, 255), (120, 200, 255), (70, 150, 250)]
}

def spawn_particles(x, y, count=8, is_trail=False):
    particles = []
    colors = SKIN["particle_colors"]
    spd_mult = 1.0 if is_trail else 1.4
    for _ in range(count):
        particles.append({
            "x": x, "y": y,
            "vx": random.uniform(-1.6, 1.6) * spd_mult,
            "vy": random.uniform(-1.2, 2.4) if not is_trail else random.uniform(-0.6, 1.0),
            "life": random.randint(9, 14) if not is_trail else random.randint(6, 9),
            "max_life": 14,
            "color": random.choice(colors),
            "type": "snowflake" if random.random() < 0.5 else "crystal",
            "size": random.choice([2, 3]) if not is_trail else 2
        })
    return particles

def update_particle(p, sim_steps):
    # Organic fluttering snowflakes drifting downwards
    p["x"] += math.sin(sim_steps * 0.2 + p["life"]) * 0.4
