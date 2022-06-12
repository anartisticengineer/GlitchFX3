from abc import abstractmethod


class GlitchFilter:
    def __init__(self, src_img, **kwargs):
        (h, w, channels) = src_img.shape
        self._h = h
        self._w = w
        self._channels = channels
        self._src_img = src_img
        self._dst_img = src_img
        self._kwarg_dict = kwargs
        self._error_msg = ''

    @property
    def dst_img(self):
        return self._dst_img

    @abstractmethod
    def apply_filter(self):
        pass
