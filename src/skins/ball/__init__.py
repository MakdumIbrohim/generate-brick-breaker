from .classic import SKIN as CLASSIC_SKIN, spawn_particles as classic_spawn, update_particle as classic_update
from .fire import SKIN as FIRE_SKIN, spawn_particles as fire_spawn, update_particle as fire_update
from .ice import SKIN as ICE_SKIN, spawn_particles as ice_spawn, update_particle as ice_update
from .lightning import SKIN as LIGHTNING_SKIN, spawn_particles as lightning_spawn, update_particle as lightning_update
from .poison import SKIN as POISON_SKIN, spawn_particles as poison_spawn, update_particle as poison_update

BALL_SKINS = {
    "classic": CLASSIC_SKIN,
    "fire": FIRE_SKIN,
    "ice": ICE_SKIN,
    "lightning": LIGHTNING_SKIN,
    "poison": POISON_SKIN,
}

BALL_SPAWNERS = {
    "classic": classic_spawn,
    "fire": fire_spawn,
    "ice": ice_spawn,
    "lightning": lightning_spawn,
    "poison": poison_spawn,
}

BALL_UPDATERS = {
    "classic": classic_update,
    "fire": fire_update,
    "ice": ice_update,
    "lightning": lightning_update,
    "poison": poison_update,
}
