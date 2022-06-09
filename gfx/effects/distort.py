import cv2 as cv
import numpy as np
from perlin_noise import PerlinNoise
from ..util.generators import *


def warp(src_img, **kwargs):
    _warp_type: str = kwargs.get('type', 'shearX')
    _factor: float = kwargs.get('f', 1.0)

    dst_img = src_img
    (h, w, _) = src_img.shape

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
        for (u, v) in pixels_generator(w, h):
            (x, y) = f(u, v)
            dst_img[x, y] = src_img[u, v]
    except KeyError:
        print('Invalid warp type (effect bypassed)')
    finally:
        return dst_img


def wavy(src_img, **kwargs):
    _octaves: int = kwargs.get('oct', 5)
    _max_scale: float = kwargs.get('scl', 0.1)

    dst_img = src_img
    (h, w, _) = src_img.shape

    pn = PerlinNoise(octaves=_octaves, seed=np.random.randint(100))

    try:
        if _octaves < 0 or not type(_octaves) is int:
            raise ValueError
        for u in x_generator(w):
            offset = int(_max_scale * h * pn([u/w]))
            col = src_img[:, u]
            shifted_col = np.vstack((col[offset:], col[:offset]))
            dst_img[:, u] = shifted_col
    except ValueError:
        print('Octave value must be a positive integer (effect bypassed)')
    finally:
        return dst_img


def burn(src_img, **kwargs):
    _percent: float = kwargs.get('p', 0.5)

    dst_img = src_img
    (h, w, _) = src_img.shape
    error_msg = 'An error occurred'

    try:
        if _percent < 0.0 or _percent > 1.0:
            error_msg = 'Percent should be between 0.0 and 1.0'
            raise ValueError
        edge_img = cv.Scharr(src_img, cv.CV_64F, dx=1, dy=0)
        gray_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
        (_, mask_img) = cv.threshold(gray_img, int(_percent * 255), 255, cv.THRESH_BINARY)
        mask_img.reshape(mask_img.shape[0], mask_img.shape[1]).astype('?')
        for (u, v) in pixels_generator(w, h):
            dst_img[u, v] = src_img[u, v] if mask_img[u, v] > 125 else edge_img[u, v]
    except ValueError:
        print(error_msg)
    finally:
        return dst_img
