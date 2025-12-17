from src.errors import ColorChipError, OtherClassError, ChipError


class Chip:
    def __init__(self, color, price, stack=1):
        if not(isinstance(color, str)) or not(isinstance(price, int)):
            raise ChipError
        self.color = color
        self.price = price
        self.stack = stack


    def __add__(self, other):
        if isinstance(other, Chip):
            if self.color == other.color:
                return Chip(self.color, self.price + other.price, self.stack + other.stack)
            else:
                raise ColorChipError
        return OtherClassError
