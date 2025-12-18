import random

from src.collections.casinobalance import CasinoBalance
from src.constants import PRICES, KEYS
from src.objects.chip import Chip
from src.errors import NotEnoughMoney, NotEnoughChips, StavkaError
from random import randint
from src.objects.goose import WarGoose, HonkGoose
from src.objects.player import Player


class Casino:

    def __init__(self, casino_balance: CasinoBalance | list[int] | None=None,
                 prices: int | None=None, seed: int | None=None):
        """
        инициализация казино
        :param casino_balance: баланс казино (количесвто фишек разного цвета)
        :param prices: цены на фишки в зависимости от цвета
        :param seed: параметр генерации
        """
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

    def buy_chips(self, other: Player, money_to_buy: int, flag: bool=False):
        """
        Покупка фишек за доллары
        :param other: игрок, совершающий данное действие
        :param money_to_buy: количество денег для покупки
        :param flag: флаг для выигрыша и проигрыша
        :return: ничего не возвращает
        """
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
                print(f"баланс фишки: {other.chip_balance}, деньги {other.money} долларов")
                print("Операция прошла успешно\n")
                return

        print(f"в казино больше нет фишек, недокуплено на {money_to_buy} долларов")

    def sell_chips(self, other: Player, money_to_sell: int, flag: bool=False) -> int:
        """
        Функция обмена фишек на доллары
        :param other: игрок, совершающий данное действие
        :param money_to_sell: деньги, которые игрок хочет вывести
        :param flag: параметр для выигрыша и проигрыша
        :return: возвращает недопроданную сумму
        """
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
            flag1 = False
            for i in range(len(other.chip_balance)):
                i -= itr
                if other.chip_balance[i].color == key:
                    flag1 = True
                    if other.chip_balance[i].stack <= target != 0:
                        target = other.chip_balance[i].stack
                        other.chip_balance.pop(i)
                        itr += 1
                    else:
                        other.chip_balance[i].stack -= target
                    other.money += target * PRICES[key]
            if flag1:
                money_to_sell -= target * PRICES[key]
                print(f"продано {target} фишек цвета {key}")
                self.casino_balance[key] += target
        if money_to_sell == 0:
            print(f"баланс фишки: {other.chip_balance}, деньги {other.money} долларов")
            print("Операция прошла успешно\n")
            return money_to_sell
        else:
            print(f"Не получается получить всю сумму: {money_to_sell} долларов не распределено")
            print(f"баланс фишки: {other.chip_balance}, деньги {other.money} долларов\n")
            return money_to_sell

    def ruletka(self, player: Player, stavka: int, typ: str | int | None=None):
        """
        Американская рулетка
        :param player: игрок, выбравший данное действие
        :param stavka: ставка в долларах
        :param typ: от 0 до 36, либо  odd/even 1st/2nd/3rd dozen
        :return: ничего не возвращает
        """
        minus = self.sell_chips(player, stavka, flag=True)
        stavka = stavka - minus
        rul = randint(0, 36)
        win = 0
        if isinstance(typ, int) and 0 <= typ <= 36:
            if rul == typ:
                win = stavka * 36
        elif typ == '1st dozen' and rul < 13:
            win = stavka * 3
        elif typ == '2nd dozen' and 13 <= rul <= 24:
            win = stavka * 3
        elif typ == '3rd dozen' and 25 <= rul <= 36:
            win = stavka * 3
        elif typ == 'odd' and rul % 2 != 0:
            win = stavka * 3
        elif typ == 'even' and rul % 2 == 0:
            win = stavka * 3
        elif typ not in ['1st dozen', '2nd dozen', '3rd dozen', 'odd', 'even']:
            raise StavkaError
        print(f"Игрок {player.name} поставил {stavka} долларов на {typ}")
        print(f"выпало {rul}")
        if win > 0:
            print(f"Он выиграл {win} долларов")
            self.buy_chips(player, win, flag=True)
        else:
            print(f"Он проиграл {stavka}\n")

    @staticmethod
    def war_goose_battle(goose: WarGoose, player: Player):
        """
        Игрок забирает у гуся доллары в борьбе
        :param goose: боевой гусь
        :param player: игрок
        """
        power = randint(0, 1000)
        goose.war(power, player)

    @staticmethod
    def honk_ring(goose: HonkGoose, player: Player):
        """
        Гусь своим криком уменьшает баланс долларов у игрока
        :param goose: кричащий гусь
        :param player: игрок
        """
        goose.honk(player)










