import cv2 as cv
import numpy as np
from perlin_noise import PerlinNoise
from ..util.generators import *


def warp(src_img, **kwargs):
    _warp_type = kwargs.get('type', 'shearX')
    _factor = kwargs.get('f', 1.0)

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
    _octaves = kwargs.get('o', 5)

    dst_img = src_img
    (h, w, _) = src_img.shape

    pn = PerlinNoise(octaves=_octaves, seed=np.random.randint(100))

    try:
        for u in x_generator(w):
            offset = int(100 * pn([u/w]))
            col = src_img[:, u]
            shifted_col = np.vstack((col[offset:], col[:offset]))
            dst_img[:, u] = shifted_col
    except ValueError:
        pass
    finally:
        return dst_img


