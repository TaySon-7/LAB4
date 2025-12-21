import pytest
from src.objects.player import Player
from src.constants import PRICES
from src.casino import Casino
from src.objects.goose import WarGoose, HonkGoose


casino = Casino([1000, 1000, 1000, 1000], PRICES, seed=102)
player = Player("Max", money=5000)
war_goose1 = WarGoose("Beliy", 1000)
war_goose2 = WarGoose("Beliy", 1500)
honk_goose1 = HonkGoose("Seriy", 500)
honk_goose2 = HonkGoose("Seriy", 200)


def test_honk_goose():
    casino.honk_ring(honk_goose1, player)
    assert player.money == 4500
    casino.honk_ring(honk_goose2, player)
    assert player.money == 4300


def test_war_goose():
    casino.war_goose_battle(war_goose1, player)
    assert player.money == 4673 or 4651
    casino.war_goose_battle(war_goose2, player)
    assert player.money == 5143 or 5040





