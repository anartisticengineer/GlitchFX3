import pytest
from numpy import random
from ..effects.distort import Warp, Wavy, Burn

sample_image = random.randint(0, 255, size=(10, 10, 3))


def test_warp_bad_key():
    with pytest.raises(KeyError):
        Warp(sample_image, **{'type': 'notAType'}).apply_filter()


def test_wavy_negative_oct():
    with pytest.raises(ValueError):
        Wavy(sample_image, **{'oct': -1}).apply_filter()


def test_burn_pct_negative():
    with pytest.raises(ValueError):
        Burn(sample_image, **{'p': -1.0}).apply_filter()


def test_burn_pct_over():
    with pytest.raises(ValueError):
        Burn(sample_image, **{'p': 1.1}).apply_filter()

