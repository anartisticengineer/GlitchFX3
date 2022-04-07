from cv2 import waitKey
from gfx.initialize import GFX
from gfx.util.argparser import ArgParser

if __name__ == '__main__':
    gfx = GFX()
    arg_parser = ArgParser()
    effect_name = None

    # Loop until exit
    while effect_name != 'x':
        (effect_name, *params) = GFX.get_effect_request()
        arg_parser.parse(*params)
        if effect_name != 'x':
            gfx.apply_effect(effect_name, **arg_parser.args)

    gfx.show_dest_image()

    # Save prompt
    k = waitKey()
    if k == ord('s') or k == ord('S'):
        gfx.save_image()

    del gfx
