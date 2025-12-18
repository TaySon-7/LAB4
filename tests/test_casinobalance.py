import pytest
from src.collections.casinobalance import CasinoBalance
from src.errors import NoChipError


def test_casino_balance():
    balance = CasinoBalance({"black": 100, "red": 50})
    assert balance.dct == {"black": 100, "red": 50}


def test_casino_balance_init_error():
    with pytest.raises(NoChipError):
        balance = CasinoBalance()


def test_casino_balance_len():
    balance = CasinoBalance({"black": 100, "red": 50})
    assert len(balance) == 2


def test_casino_balance_getitem():
    balance = CasinoBalance({"black": 100, "red": 50})
    assert balance["black"] == 100


def test_casino_balance_getitem_error():
    balance = CasinoBalance({"black": 100, "red": 50})
    with pytest.raises(IndexError):
        assert balance["pink"] == 100


def test_casino_balance_setitem():
    balance = CasinoBalance({"black": 100, "red": 50})
    balance["black"] = 500
    assert balance["black"] == 500


def test_casino_balance_del():
    balance = CasinoBalance({"black": 100, "red": 50})
    balance.delete("red")
    assert len(balance) == 1


def test_casino_balance_del_error():
    balance = CasinoBalance({"black": 100, "red": 50})
    with pytest.raises(IndexError):
        balance.delete("pink")
        assert len(balance) == 1
