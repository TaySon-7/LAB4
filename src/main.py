from src.objects.player import Player
from src.constants import PRICES
from casino import Casino

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
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
    player = Player(money=balance)
    print(player.money)
    casino.buy_chips(player, 855)
    casino.sell_chips(player, 550)






if __name__ == "__main__":
    main()
