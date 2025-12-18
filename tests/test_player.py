import pytest
from src.objects.player import Player

def test_player():
    player = Player('Max', money=1000)
    assert player.name == 'Max'
    assert player.money == 1000