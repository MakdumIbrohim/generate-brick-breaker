from src.skins.ball import BALL_SPAWNERS, BALL_UPDATERS
from src.skins.paddle import PADDLE_IMPACT_SPAWNERS

def create_ball_particles(skin, x, y, count=8, is_trail=False):
    sname = skin.get("name", "classic")
    spawner = BALL_SPAWNERS.get(sname)
    if spawner:
        return spawner(x, y, count=count, is_trail=is_trail)
    return []

def create_paddle_impact_particles(paddle_skin, ball_skin, hit_x, paddle_y, hit_offset):
    pname = paddle_skin.get("name", "default")
    spawner = PADDLE_IMPACT_SPAWNERS.get(pname)
    if spawner:
        return spawner(ball_skin, hit_x, paddle_y, hit_offset)
    return []

def update_particles(particles, sim_steps):
    surviving = []
    for p in particles:
        p["x"] += p["vx"]
        p["y"] += p["vy"]

        # Delegate update physics by type
        ptype = p.get("type")
        if ptype in ("spark", "ember"):
            BALL_UPDATERS["fire"](p, sim_steps)
        elif ptype in ("snowflake", "crystal"):
            BALL_UPDATERS["ice"](p, sim_steps)
        elif ptype == "zap":
            BALL_UPDATERS["lightning"](p, sim_steps)
        elif ptype == "bubble":
            BALL_UPDATERS["poison"](p, sim_steps)

        p["life"] -= 1
        if p["life"] > 0:
            surviving.append(p)
    return surviving
