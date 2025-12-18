import pytest
from src.collections.chipcollection import ChipCollection


def test_chip_collection():
    col = ChipCollection([1, 2, 4, 5])
    assert col.lst == [1, 2, 4, 5]


def test_collection_len():
    col = ChipCollection([1, 2, 4, 5])
    assert len(col) == 4


def test_collection_add():
    col = ChipCollection([1, 2, 4, 5])
    col.add(100)
    assert col[-1] == 100


def test_collection_slice():
    col = ChipCollection([1, 2, 4, 5])
    col1 = col[2:4]
    assert len(col1) == 2


def test_collection_setitem():
    col = ChipCollection([1, 2, 4, 5])
    col[-1] = 100
    assert col[-1] == 100


def test_collection_pop():
    col = ChipCollection([1, 2, 4, 5])
    col.pop(-1)
    assert col[-1] == 4


def test_collection_pop_error():
    col = ChipCollection([1, 2, 4, 5])
    with pytest.raises(IndexError):
        col.pop(100)





