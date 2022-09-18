import pytest
from numpy import random
from ..effects.basic import Noisy, Scanlines, Scanner

sample_image = random.randint(0, 255, size=(10, 10, 3))


def test_noisy_pct_negative():
    with pytest.raises(ValueError):
        Noisy(sample_image, **{'p': -0.1}).apply_filter()


def test_noisy_pct_over():
    with pytest.raises(ValueError):
        Noisy(sample_image, **{'p': 1.1}).apply_filter()


def test_noisy_pct_not_float():
    with pytest.raises(TypeError):
        Noisy(sample_image, **{'p': 'zero'}).apply_filter()


def test_scanlines_or():
    with pytest.raises(KeyError):
        Scanlines(sample_image, **{'or': 'x'}).apply_filter()


def test_scanner_or():
    with pytest.raises(KeyError):
        Scanner(sample_image, **{'or': 'x'}).apply_filter()


def test_scanner_pct_negative():
    with pytest.raises(ValueError):
        Scanner(sample_image, **{'p': -0.1}).apply_filter()


def test_scanner_pct_over():
    with pytest.raises(ValueError):
        Scanner(sample_image, **{'p': 1.1}).apply_filter()


def test_scanner_pct_not_float():
    with pytest.raises(TypeError):
        Scanner(sample_image, **{'p': 'zero'}).apply_filter()