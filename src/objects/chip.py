from collections.abc import Callable
from typing import Self
from src.errors import ColorChipError, OtherClassError, ChipError


class Chip:
    def __init__(self, color: str, price: int, stack: int = 1):
        """
        Инициализация фишки
        :param color: цвет фишки
        :param price: цена фишки за единицу
        :param stack: количесвто фишек в стопке
        """
        if not(isinstance(color, str)) or not(isinstance(price, int)):
            raise ChipError
        self.color = color
        self.price = price
        self.stack = stack


    def __add__(self, other: Self):
        """
        Сложение двух стопок фишек в одну
        :param other: дргая стопка фишек
        :return: ничего не возвращает
        """
        if isinstance(other, Chip):
            if self.color == other.color:
                return Chip(self.color, self.price, self.stack + other.stack)
            else:
                raise ColorChipError
        raise OtherClassError
