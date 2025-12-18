

from src.objects.player import Player
from src.constants import PRICES, COMMANDS
from casino import Casino

def main() -> None:
    """
    Точка входы в казино
    :return: Данная функция ничего не возвращает
    """
    token = None
    print("Вас приветствует казино Московского авиационного института")
    print("Чтобы начать игру, введите баланс казино в целочисленной форме по каждому цвету фишек: белые, красные, зеленые, черные")
    while token is None:
        try:
            token = list(map(int, input().split()))
        except ValueError:
            print("баланс должен быть целочисленным")
    casino = Casino(token, PRICES)
    print(casino.casino_balance)
    print(casino.prices)
    print("Теперь задайте ваш баланс в долларах")
    balance = None
    while balance is None:
        try:
            balance = int(input())
        except ValueError:
            print("баланс должен быть целочисленным")
    print("Введите ваше имя")
    name = None
    while name is None:
        try:
            name = input()
        except ValueError:
            print("вы должны ввести ваше имя")
    player = Player(name, money=balance)
    print("Далее выбирайте из 3 команд: buy [int], sell [int], ruletka [int] [int or str] - все вводится в долларах через пробел")
    while True:
        token = input().split()
        if len(token) == 1:
            if token[0] == 'exit':
                break
        elif len(token) == 2:
            if token[0] == "buy":
                casino.buy_chips(player, int(token[1]))
            elif token[0] == "sell":
                casino.sell_chips(player, int(token[1]))
            else:
                print("Неккоректная команда")
        elif len(token) == 3:
            if token[0] == "ruletka":
                try:
                    casino.ruletka(player, int(token[1]), int(token[2]))
                except ValueError:
                    casino.ruletka(player, int(token[1]), token[2])
            else:
                print("Неккоректная команда")
        else:
            print("Неккоректная команда")







if __name__ == "__main__":
    main()
