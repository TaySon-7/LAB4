import random
from random import randint

from src.objects.player import Player
from src.constants import PRICES
from casino import Casino

operations = ["buy chips", "sell chips", "rul_stavka_1", "rul_stavka_2", "rul_stavka_3"]

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    casino = Casino([1000, 1000, 1000, 1000], PRICES, seed)
    players = []
    names = ["Maxima", "Fedora", "Artemida", "Vlada" ]
    print("Инициализация игроков и их балансов\n")
    for i in range(4):
        players.append(Player(name=names[i], money=100000))
        casino.buy_chips(players[i], 5000)
    print("Начало игры")
    for i in range(steps):
        print(f"шаг {i + 1}")
        player = random.choice(players)
        oper = random.choice(operations)
        if oper ==  operations[0]:
            money_to_buy = randint(1, 1000)
            casino.buy_chips(player, money_to_buy)
        elif oper == operations[1]:
            money_to_sell = randint(1, 1000)
            casino.sell_chips(player, money_to_sell)
        elif oper == operations[2]:
            stavka = randint(1, 1000)
            typ = randint(0, 36)
            casino.ruletka(player, stavka, typ)
        elif oper == operations[3]:
            stavka = randint(1, 1000)
            typ = random.choice(["1st dozen", '2nd dozen', '3rd dozen'])
            casino.ruletka(player, stavka, typ)
        elif oper == operations[4]:
            stavka = randint(1, 1000)
            typ = random.choice(["odd", "even"])
            casino.ruletka(player, stavka, typ)


run_simulation()

