from src.collections.chipcollection import ChipCollection
from src.errors import PlayerError


class Player:
    def __init__(self, name, chip_balance=None, money=0):
        if chip_balance is not None and (not(isinstance(chip_balance, ChipCollection))
                                         or not(isinstance(money, int))):
            raise PlayerError
        self.money = money
        self.chip_balance = ChipCollection(chip_balance) if chip_balance is not None else ChipCollection()
        self.name = name
