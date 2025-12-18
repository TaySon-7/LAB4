import pytest
from src.objects.chip import Chip
from src.errors import ColorChipError

def test_chip_add():
    chip = Chip("black", 100)
    chip_new = Chip("black", 2000)
    assert chip.price == 100
    assert chip.stack == 1
    assert  chip.color == "black"
    assert  (chip + chip_new).stack == 2

def test_chip_add_error():
    chip = Chip("black", 100)
    chip_new = Chip("red", 2000)
    with pytest.raises(ColorChipError):
        chip + chip_new

