import pytest
from ..util.argparser import ArgParser

parser = ArgParser()


def test_one():
    parser.parse('p 0')
    assert parser.args == {'p': 0}


def test_two_params():
    parser.parse('p 0', 'k 3', 't vertical')
    assert parser.args == {'p': 0, 'k': 3, 't': 'vertical'}


def test_too_many():
    with pytest.raises(Exception):
        parser.parse('p 0 1')


def test_empty_again():
    assert parser.args == {}


def test_invalid_type():
    with pytest.raises(Exception):
        parser.parse(0)
