import cv2 as cv
import numpy as np


def noisy(src_img, **kwargs):
    _percent: float = kwargs.get('p', 0.1)
    try:
        if _percent < 0.0 or _percent > 1.0:
            raise ValueError
        if not type(_percent) is float:
            raise TypeError
    except ValueError:
        print('Percent value should be between 0.0 and 1.0')
        return src_img
    except TypeError:
        print('Percent value should be a float value')
        return src_img
    else:
        (x, y, z) = src_img.shape
        poisson = np.random.poisson(_percent * 100, src_img.size)
        poisson = poisson.reshape(x, y, z).astype(np.uint8)
        dst_img = cv.add(src_img, poisson)
        return dst_img


def scan_lines(src_img, **kwargs):
    _orientation = kwargs.get('or', 'h')

    orientation_dict = {'h': 0, 'v': 1}
    try:
        max_i = src_img.shape[orientation_dict[_orientation]]
        if _orientation == 'h':
            src_img[0:max_i:2] = [0, 0, 0]
        elif _orientation == 'v':
            src_img[:, 0:max_i:2] = [0, 0, 0]
    except KeyError:
        print('Invalid orientation (effect bypassed)')
    finally:
        return src_img


def high_pass(src_img, **kwargs):
    _percent = kwargs.get('p', 0.5)
    _kernel_size = kwargs.get('k', 3)
    _amp = kwargs.get('a', 1.0)

    error_msg = ''
    try:
        _kernel_size = int(_kernel_size)
        if _percent < 0.0 or _percent > 1.0:
            error_msg = 'Percent should be between 0.0 and 1.0'
            raise ValueError
        if not type(_percent) is float:
            error_msg = 'Percent value should be a float value'
            raise TypeError
        if _kernel_size % 2 != 1:
            error_msg = 'Invalid Kernel Size'
            raise ValueError
    except (TypeError, ValueError):
        print(error_msg)
        return src_img
    else:
        midpoint = int(_kernel_size/2)
        filter_kernel = np.ones((_kernel_size, _kernel_size), dtype=np.float32)
        filter_kernel *= (-1.0 * _percent)
        filter_kernel[midpoint, midpoint] = (_kernel_size * 2) * _amp
        dst_img = cv.filter2D(src_img, -1, filter_kernel)

        return dst_img
