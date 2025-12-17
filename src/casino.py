from src.collections.casinobalance import CasinoBalance
from src.constants import PRICES, KEYS
from src.objects.chip import Chip
from src.errors import NotEnoughMoney, NotEnoughChips


class Casino:

    def __init__(self, casino_balance=None, prices=None):
        if isinstance(casino_balance, list):
            dct = {}
            for value, key in zip(casino_balance, PRICES.keys()):
                dct[key] = value
            self.casino_balance = CasinoBalance(dct)
        else:
            self.casino_balance = casino_balance
        self.prices = prices

    def buy_chips(self, other, money_to_buy):
        if other.money < money_to_buy:
            raise NotEnoughMoney
        keys = KEYS
        for key in keys:
            target = money_to_buy // PRICES[key]
            if target > self.casino_balance[key]:
                target = self.casino_balance[key]
            other.money -= target * PRICES[key]
            money_to_buy -= target * PRICES[key]
            chip = Chip(color=key, price=PRICES[key], stack=target)
            flag = False
            for i in range(len(other.chip_balance)):
                if other.chip_balance[i].color == key:
                    other.chip_balancee[i] = other.chip_balance[i] + chip
                    flag = True
                    print(f"добавилась стопка {chip.stack} фишек цвета {chip.color}")
            if not flag:
                other.chip_balance.add(chip)
                print(f"добавилась стопка {chip.stack} фишек цвета {chip.color}")
            if money_to_buy == 0:
                print("Операция прошла успешно")
                return

        print(f"в казино больше нет фишек, недокуплено на {money_to_buy}")

    def sell_chips(self, other, money_to_sell):
        dollars = 0
        for chip in other.chip_balance:
            dollars += chip.stack * chip.price
        if dollars < money_to_sell:
            raise NotEnoughChips
        keys = KEYS
        for key in keys:
            target = money_to_sell // PRICES[key]
            for i in range(len(other.chip_balance)):
                if other.chip_balance[i].color == key:
                    if other.chip_balance[i].stack < target:
                        target = other.chip_balance[i].stack
                        other.chip_balance.pop(i)
                    else:
                        other.chip_balance[i].stack -= target
            money_to_sell -= target * PRICES[key]
            if target > 0:
                print(f"продано {target} фишек цвета {key}")
            self.casino_balance[key] += target
        if money_to_sell == 0:
            print("Операция прошла успешно")

    def ruletka(self, player, stavka):
        pass






