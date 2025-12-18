from src.collections.chipcollection import ChipCollection
from src.errors import PlayerError


class Player:
    def __init__(self, name: str, chip_balance: ChipCollection | None =None, money: int = 0):
        """
        Инициализация игрока
        :param name: имя игрока
        :param chip_balance: баланс игрока в фишках (коллекция фишек)
        :param money: баланс игрока в долларах
        """
        if chip_balance is not None and (not(isinstance(chip_balance, ChipCollection))
                                         or not(isinstance(money, int))):
            raise PlayerError
        self.money = money
        self.chip_balance = ChipCollection(chip_balance) if chip_balance is not None else ChipCollection()
        self.name = name
