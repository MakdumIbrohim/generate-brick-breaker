from .classic import THEME as CLASSIC_THEME, init_ambient as classic_init, update_ambient as classic_update
from .sky import THEME as SKY_THEME, init_ambient as sky_init, update_ambient as sky_update
from .sky_night import THEME as SKY_NIGHT_THEME, init_ambient as sky_night_init, update_ambient as sky_night_update
from .synthwave import THEME as SYNTHWAVE_THEME, init_ambient as synth_init, update_ambient as synth_update
from .matrix import THEME as MATRIX_THEME, init_ambient as matrix_init, update_ambient as matrix_update

THEMES = {
    "classic": CLASSIC_THEME,
    "sky": SKY_THEME,
    "sky-night": SKY_NIGHT_THEME,
    "synthwave": SYNTHWAVE_THEME,
    "matrix": MATRIX_THEME,
}

THEME_INITIALIZERS = {
    "classic": classic_init,
    "sky": sky_init,
    "sky-night": sky_night_init,
    "synthwave": synth_init,
    "matrix": matrix_init,
}

THEME_UPDATERS = {
    "classic": classic_update,
    "sky": sky_update,
    "sky-night": sky_night_update,
    "synthwave": synth_update,
    "matrix": matrix_update,
}
