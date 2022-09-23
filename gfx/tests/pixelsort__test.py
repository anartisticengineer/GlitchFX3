import pytest
from numpy import random
from ..effects.pixelsort_special import PSort

sample_image = random.randint(0, 255, size=(10, 10, 3))


def test_ps_upper_above_lower():
    with pytest.raises(ValueError):
        PSort(sample_image, **{'lower': 0.7, 'upper': 0.3}).apply_filter()


def test_ps_lower_negative():
    with pytest.raises(ValueError):
        PSort(sample_image, **{'lower': -0.1}).apply_filter()


def test_ps_upper_above():
    with pytest.raises(ValueError):
        PSort(sample_image, **{'upper': 1.1}).apply_filter()


def test_ps_bad_key():
    with pytest.raises(KeyError):
        PSort(sample_image, **{'or': 'x'}).apply_filter()

