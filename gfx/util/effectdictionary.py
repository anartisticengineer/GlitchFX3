from ..effects import basic, distort

effect_dictionary = {'noisy': basic.noisy,
                     'highpass': basic.high_pass,
                     'scanlines': basic.scan_lines,
                     'warp': distort.warp,
                     'wavy': distort.wavy,
                     'burn': distort.burn
                     }
