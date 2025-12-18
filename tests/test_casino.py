import pytest
from src.objects.player import Player
from src.constants import PRICES
from src.casino import Casino
from src.errors import NotEnoughChips, NotEnoughMoney, StavkaError

casino = Casino([1000, 1000, 1000, 1000], PRICES, seed=102)

player = Player("Max", money=5000)

def test_casino_buy_chips():
    casino.buy_chips(player, 2556)
    assert player.money == 2444
    assert player.chip_balance[0].stack == 25
    assert player.chip_balance[0].color == "black"
    assert player.chip_balance[0].price == 100
    assert player.chip_balance[1].stack == 2
    assert player.chip_balance[1].color == "green"
    assert player.chip_balance[1].price == 25


def test_casino_sell_chips():
    casino.sell_chips(player, 2556)
    assert player.money == 5000
    assert len(player.chip_balance) == 0


def test_casino_ruletka():
    casino.buy_chips(player, 5000)
    casino.ruletka(player, 1000, typ=9)
    casino.sell_chips(player, 40000)
    assert player.money == 41000


def test_sell_error():
    with pytest.raises(NotEnoughMoney):
        casino.buy_chips(player, 50000)


def test_chip_error():
    with pytest.raises(NotEnoughChips):
        casino.sell_chips(player, 100000)


def test_stavka_error():
    casino.buy_chips(player, 1000)
    with pytest.raises(StavkaError):
        casino.ruletka(player, stavka=1000, typ=404)
