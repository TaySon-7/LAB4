from src.objects.player import Player


class Goose:
    def __init__(self, name, honk_volume):
        self.name = name
        self.honk_volume = honk_volume


class WarGoose(Goose):
    def __init__(self, name, honk_volume):
        super().__init__(name, honk_volume)

    def war(self, power:int, player: Player):
        player.money += power
        print(f"Боевой Гусь {self.name} атакует игрока {player.name}, в итоге игрок отобрал {power} долларов")
        print(f"баланс {player.money} долларов\n")

class HonkGoose(Goose):
    def __init__(self, name, honk_volume):
        super().__init__(name, honk_volume)

    def honk(self, player: Player):
        target = self.honk_volume
        if target > player.money:
            target = player.money
        player.money -= target
        print(f"Гусь {self.name} криком выбил из кошелька игрока {player.name} денег на сумму {target}")
        print(f"баланс {player.money} долларов\n")


