from .classic import THEME as CLASSIC_THEME, init_ambient as classic_init, update_ambient as classic_update
from .sky import THEME as SKY_THEME, init_ambient as sky_init, update_ambient as sky_update
from .sky_night import THEME as SKY_NIGHT_THEME, init_ambient as sky_night_init, update_ambient as sky_night_update
from .synthwave import THEME as SYNTHWAVE_THEME, init_ambient as synth_init, update_ambient as synth_update
from .matrix import THEME as MATRIX_THEME, init_ambient as matrix_init, update_ambient as matrix_update
from .sakura import THEME as SAKURA_THEME, init_ambient as sakura_init, update_ambient as sakura_update

THEMES = {
    "classic": CLASSIC_THEME,
    "sky": SKY_THEME,
    "sky-night": SKY_NIGHT_THEME,
    "synthwave": SYNTHWAVE_THEME,
    "matrix": MATRIX_THEME,
    "sakura": SAKURA_THEME,
}

THEME_INITIALIZERS = {
    "classic": classic_init,
    "sky": sky_init,
    "sky-night": sky_night_init,
    "synthwave": synth_init,
    "matrix": matrix_init,
    "sakura": sakura_init,
}

THEME_UPDATERS = {
    "classic": classic_update,
    "sky": sky_update,
    "sky-night": sky_night_update,
    "synthwave": synth_update,
    "matrix": matrix_update,
    "sakura": sakura_update,
}

def hex_to_rgb(hex_str):
    h = hex_str.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) == 6:
        try:
            return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
        except ValueError:
            return None
    return None

def parse_custom_brick_colors(color_str):
    if not color_str or color_str.strip() in ("", "none", "null"):
        return None
    parts = [p.strip() for p in color_str.split(",") if p.strip()]
    rgbs = [hex_to_rgb(p) for p in parts]
    rgbs = [c for c in rgbs if c is not None]
    if len(rgbs) >= 4:
        return rgbs[:4]
    if len(rgbs) == 1:
        r, g, b = rgbs[0]
        return [
            (max(15, int(r * 0.28)), max(15, int(g * 0.28)), max(15, int(b * 0.28))),
            (int(r * 0.50), int(g * 0.50), int(b * 0.50)),
            (int(r * 0.75), int(g * 0.75), int(b * 0.75)),
            (r, g, b),
        ]
    return None
