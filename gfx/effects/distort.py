import cv2 as cv
import numpy as np
from perlin_noise import PerlinNoise
from ..util.generators import *
from .filter import GlitchFilter


class Warp(GlitchFilter):
    def apply_filter(self):
        _warp_type: str = self._kwarg_dict.get('type', 'shearX')
        _factor: float = self._kwarg_dict.get('f', 1.0)
        (w, h) = (self._w, self._h)

        def shear_x(_u, _v):
            return _u, (_u + int(_factor * _v)) % w

        def shear_y(_u, _v):
            return (_u + int(_factor * _v)) % h, _v

        def rotate_x(_u, _v):
            return _u, int(_u * np.sin(_factor) + _v * np.cos(_factor)) % w

        def rotate_y(_u, _v):
            return int(_u * np.cos(_factor) - _v * np.sin(_factor)) % h, _v

        f_dict = {'shearX': shear_x, 'shearY': shear_y, 'rotateX': rotate_x, 'rotateY': rotate_y}

        try:
            f = f_dict[_warp_type]
            for (u, v) in pixels_generator(self._w, self._h):
                (x, y) = f(u, v)
                self._dst_img[x, y] = self._src_img[u, v]
        except KeyError:
            print('Invalid warp type (effect bypassed)')


class Wavy(GlitchFilter):
    def apply_filter(self):
        _octaves: int = self._kwarg_dict.get('oct', 5)
        _max_scale: float = self._kwarg_dict.get('scl', 0.1)

        pn = PerlinNoise(octaves=_octaves, seed=np.random.randint(100))

        try:
            if _octaves < 0:
                raise ValueError
            for u in x_generator(self._w):
                offset = int(_max_scale * self._h * pn([u / self._w]))
                col = self._src_img[:, u]
                shifted_col = np.vstack((col[offset:], col[:offset]))
                self._dst_img[:, u] = shifted_col
        except ValueError:
            print('Octave value must be a positive integer (effect bypassed)')


class Burn(GlitchFilter):
    def apply_filter(self):
        _percent: float = self._kwarg_dict.get('p', 0.5)

        self._error_msg = 'An error occurred'

        try:
            if _percent < 0.0 or _percent > 1.0:
                self._error_msg = 'Percent should be between 0.0 and 1.0'
                raise ValueError
            edge_img = cv.Scharr(self._src_img, cv.CV_64F, dx=1, dy=0)
            gray_img = cv.cvtColor(self._src_img, cv.COLOR_BGR2GRAY)
            (_, mask_img) = cv.threshold(gray_img, int(_percent * 255), 255, cv.THRESH_BINARY)
            mask_img.reshape(mask_img.shape[0], mask_img.shape[1]).astype('?')
            for (u, v) in pixels_generator(self._w, self._h):
                self._dst_img[u, v] = self._src_img[u, v] if mask_img[u, v] > 125 else edge_img[u, v]
        except ValueError:
            print(self._error_msg)
