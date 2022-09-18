from ..effects.basic import Noisy, Scanlines, Highpass, Scanner
from ..effects.distort import Warp, Wavy, Burn

effect_dictionary = {'noisy': Noisy,
                     'highpass': Highpass,
                     'scanlines': Scanlines,
                     'scanner': Scanner,
                     'warp': Warp,
                     'wavy': Wavy,
                     'burn': Burn
                     }
