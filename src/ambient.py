from src.themes import THEME_INITIALIZERS, THEME_UPDATERS

def init_ambient_effects(theme, canvas_w, canvas_h):
    tname = theme.get("name", "dark")
    initializer = THEME_INITIALIZERS.get(tname)
    if initializer:
        return initializer(canvas_w, canvas_h)
    return []

def update_ambient_effects(items, effect, sim_steps, canvas_w, canvas_h):
    for tname, updater in THEME_UPDATERS.items():
        if effect == THEMES_EFFECT_MAP.get(tname):
            updater(items, sim_steps, canvas_w, canvas_h)
            break

THEMES_EFFECT_MAP = {
    "dark": "starfield",
    "sky": "mario_sky",
    "synthwave": "neon_grid",
    "matrix": "matrix_rain",
}
