import cv2 as cv
import numpy as np
from .filter import GlitchFilter


class Noisy(GlitchFilter):
    def apply_filter(self):
        _percent: float = self._kwarg_dict.get('p', 0.1)
        try:
            if _percent < 0.0 or _percent > 1.0:
                raise ValueError
            if not type(_percent) is float:
                raise TypeError
        except ValueError:
            print('Percent value should be between 0.0 and 1.0')
        except TypeError:
            print('Percent value should be a float value')
        else:
            poisson = np.random.poisson(_percent * 100, self._src_img.size)
            poisson = poisson.reshape(self._h, self._w, self._channels).astype(np.uint8)
            self._dst_img = cv.add(self._src_img, poisson)


class Scanlines(GlitchFilter):
    def apply_filter(self):
        _orientation: str = self._kwarg_dict.get('or', 'h')
        orientation_dict = {'h': 0, 'v': 1}
        try:
            max_i = self._src_img.shape[orientation_dict[_orientation]]
            if _orientation == 'h':
                self._dst_img[0:max_i:2] = [0, 0, 0]
            elif _orientation == 'v':
                self._dst_img[:, 0:max_i:2] = [0, 0, 0]
        except KeyError:
            print('Invalid orientation (effect bypassed)')


class Highpass(GlitchFilter):
    def apply_filter(self):
        _percent: float = self._kwarg_dict.get('p', 0.5)
        _kernel_size: int = self._kwarg_dict.get('k', 3)
        _amp: float = self._kwarg_dict.get('a', 1.0)

        self._error_msg = 'An error occurred'

        try:
            _kernel_size = int(_kernel_size)
            if _percent < 0.0 or _percent > 1.0:
                self._error_msg = 'Percent should be between 0.0 and 1.0'
                raise ValueError
            if not type(_percent) is float:
                self._error_msg = 'Percent value should be a float value'
                raise TypeError
            if _kernel_size % 2 != 1:
                self._error_msg = 'Invalid Kernel Size'
                raise ValueError
        except (TypeError, ValueError):
            print(self._error_msg)
        else:
            midpoint = int(_kernel_size / 2)
            filter_kernel = np.ones((_kernel_size, _kernel_size), dtype=np.float32)
            filter_kernel *= (-1.0 * _percent)
            filter_kernel[midpoint, midpoint] = (_kernel_size * 2) * _amp
            self._dst_img = cv.filter2D(self._src_img, -1, filter_kernel)
