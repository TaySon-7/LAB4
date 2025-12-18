import random

from src.collections.casinobalance import CasinoBalance
from src.constants import PRICES, KEYS
from src.objects.chip import Chip
from src.errors import NotEnoughMoney, NotEnoughChips, StavkaError
from random import randint

class Casino:

    def __init__(self, casino_balance=None, prices=None, seed=None):
        if isinstance(casino_balance, list):
            dct = {}
            for value, key in zip(casino_balance, PRICES.keys()):
                dct[key] = value
            self.casino_balance = CasinoBalance(dct)
        else:
            self.casino_balance = casino_balance
        self.prices = prices
        if seed is not None:
            random.seed(seed)
        else:
            random.seed()

    def buy_chips(self, other, money_to_buy, flag=False):
        if other.money < money_to_buy and flag is False:
            raise NotEnoughMoney
        keys = KEYS
        if flag:
            print(f"Игрок {other.name} получает фишки на {money_to_buy} долларов")
        else:
            print(f"Игрок {other.name} покупает фишки на {money_to_buy} долларов")
        for key in keys:
            target = money_to_buy // PRICES[key]
            if target > self.casino_balance[key]:
                target = self.casino_balance[key]
            if not flag:
                other.money -= target * PRICES[key]
            money_to_buy -= target * PRICES[key]
            self.casino_balance[key] -= target
            chip = Chip(color=key, price=PRICES[key], stack=target)
            flag = False
            for i in range(len(other.chip_balance)):
                if other.chip_balance[i].color == key:
                    other.chip_balance[i] = other.chip_balance[i] + chip
                    flag = True
                    print(f"добавилась стопка {chip.stack} фишек цвета {chip.color}")
            if not flag:
                other.chip_balance.add(chip)
                print(f"добавилась стопка {chip.stack} фишек цвета {chip.color}")
            if money_to_buy == 0:
                print("Операция прошла успешно\n")
                return

        print(f"в казино больше нет фишек, недокуплено на {money_to_buy} долларов")

    def sell_chips(self, other, money_to_sell, flag=None):
        dollars = 0
        for chip in other.chip_balance:
            dollars += chip.stack * chip.price
        if dollars < money_to_sell:
            raise NotEnoughChips
        keys = KEYS
        if flag:
            print(f"Игрок {other.name} отдаёт фишки на {money_to_sell} долларов")
        else:
            print(f"Игрок {other.name} продаёт фишки на {money_to_sell} долларов")
        for key in keys:
            target = money_to_sell // PRICES[key]
            itr = 0
            for i in range(len(other.chip_balance)):
                i -= itr
                if other.chip_balance[i].color == key:
                    if other.chip_balance[i].stack <= target != 0:
                        target = other.chip_balance[i].stack
                        other.chip_balance.pop(i)
                        itr += 1
                    else:
                        other.chip_balance[i].stack -= target
                    if flag is None:
                        other.money += target * PRICES[key]
            money_to_sell -= target * PRICES[key]
            if target > 0:
                print(f"продано {target} фишек цвета {key}")
            self.casino_balance[key] += target
        if flag:
            money_to_sell = 0
        if money_to_sell == 0:
            print("Операция прошла успешно\n")

    def ruletka(self, player, stavka, typ=None):
        rul = randint(0, 36)
        win = 0
        if isinstance(typ, int) and 0 <= typ <= 36:
            if rul == typ:
                win = stavka * 35
        elif typ == '1st dozen' and rul < 13:
            win = stavka * 2
        elif typ == '2nd dozen' and 13 <= rul <= 24:
            win = stavka * 2
        elif typ == '3rd dozen' and 25 <= rul <= 36:
            win = stavka * 2
        elif typ == 'odd' and rul % 2 != 0:
            win = stavka * 2
        elif typ == 'even' and rul % 2 == 0:
            win = stavka * 2
        elif typ not in ['1st dozen', '2nd dozen', '3rd dozen', 'odd', 'even']:
            raise StavkaError
        print(f"Игрок {player.name} поставил {stavka} долларов на {typ}")
        print(f"выпало {rul}")
        if win > 0:
            print(f"Он выиграл {win} долларов")
            self.buy_chips(player, win, flag=True)
        else:
            print(f"Он проиграл {stavka}")
            self.sell_chips(player, stavka, flag=True)










