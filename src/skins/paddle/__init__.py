from .default import SKIN as DEFAULT_PADDLE, spawn_impact as default_impact
from .laser import SKIN as LASER_PADDLE, spawn_impact as laser_impact
from .retro import SKIN as RETRO_PADDLE, spawn_impact as retro_impact
from .mecha import SKIN as MECHA_PADDLE, spawn_impact as mecha_impact
from .cyber import SKIN as CYBER_PADDLE, spawn_impact as cyber_impact

PADDLE_SKINS = {
    "default": DEFAULT_PADDLE,
    "laser": LASER_PADDLE,
    "retro": RETRO_PADDLE,
    "mecha": MECHA_PADDLE,
    "cyber": CYBER_PADDLE,
}

PADDLE_IMPACT_SPAWNERS = {
    "default": default_impact,
    "laser": laser_impact,
    "retro": retro_impact,
    "mecha": mecha_impact,
    "cyber": cyber_impact,
}
