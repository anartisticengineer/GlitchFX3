import cv2 as cv
import numpy as np
from PIL import Image
from pixelsort import pixelsort
from .filter import GlitchFilter


class PSort(GlitchFilter):
    def apply_filter(self):
        converted_img = cv.cvtColor(self._src_img, cv.COLOR_BGR2RGB)
        pil_img = Image.fromarray(converted_img)
        pixelsorted = pixelsort(pil_img)
        opencv_img = np.array(pixelsorted)
        self._dst_img = cv.cvtColor(opencv_img, cv.COLOR_RGB2BGR)

