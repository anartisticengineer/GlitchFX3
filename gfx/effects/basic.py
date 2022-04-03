import cv2 as cv
import numpy as np


def high_pass(src_img, **kwargs):
    _kernel_size = kwargs.get('k_size', 3)
    filter_kernel = np.zeros((_kernel_size, _kernel_size))
    dst_img = cv.filter2D(src_img, -1, filter_kernel)
    return dst_img
