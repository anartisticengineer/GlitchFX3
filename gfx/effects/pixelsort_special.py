import cv2 as cv
import numpy as np
from PIL import Image
from pixelsort import pixelsort
from .filter import GlitchFilter


class PSort(GlitchFilter):
    def apply_filter(self):
        _lower: float = self._kwarg_dict.get('lower', 0.1)
        _upper: float = self._kwarg_dict.get('upper', 0.9)
        _sort_by: str = self._kwarg_dict.get('sortby', 'lightness')
        _orientation: str = self._kwarg_dict.get('or', 'h')

        angle_dict = {'h': 0, 'v': 90}

        try:
            orientation_angle = angle_dict[_orientation]
            if _lower > _upper:
                self._error_msg = 'Lower threshold value can\'t exceed upper value'
                raise ValueError
            elif _lower < 0.0 or _upper < 0.0:
                self._error_msg = 'Threshold value(s) can\'t be negative'
                raise ValueError
            elif _lower > 1.0 or _upper > 1.0:
                self._error_msg = 'Threshold value(s) can\'t exceed 1.0'
                raise ValueError
            converted_img = cv.cvtColor(self._src_img, cv.COLOR_BGR2RGB)
            pil_img = Image.fromarray(converted_img)
            pixelsorted = pixelsort(pil_img,
                                    sorting_function=_sort_by,
                                    lower_threshold=_lower,
                                    upper_threshold=_upper,
                                    angle=orientation_angle
                                    )
            opencv_img = np.array(pixelsorted)
            self._dst_img = cv.cvtColor(opencv_img, cv.COLOR_RGB2BGR)
        except ValueError:
            print(self._error_msg)
            raise
        except KeyError:
            self._error_msg = 'Invalid orientation'
            print(self._error_msg)
            raise

