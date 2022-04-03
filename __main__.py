from gfx.initialize import GFX
from gfx.util.argparser import ArgParser

if __name__ == '__main__':
    gfx = GFX()
    effect_name = None

    # Loop until exit
    while effect_name != 'x':
        (effect_name, *params) = GFX.get_effect_request()
        if effect_name != 'x':
            gfx.apply_effect(effect_name)
    del gfx
