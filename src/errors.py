class ColorChipError(Exception):
    def __init__(self):
        super().__init__(f'Нельзя складывать фишки разных цветов')

class ChipError(Exception):
    def __init__(self):
        super().__init__(f'цвет фишки должен быть строкой, а цена целочисленной')

class OtherClassError(Exception):
    def __init__(self):
        super().__init__(f'Нельзя складывать объекты разных классов')

class NoChipError(Exception):
    def __init__(self):
        super().__init__(f'Баланс казино должен быть больше нуля и словарем вида: цвет фишки - ')

class PlayerError(Exception):
    def __init__(self):
        super().__init__(f'Фишки игрока должны быть в ChipCollection, а баланс - целочисленным')

class NotEnoughMoney(Exception):
    def __init__(self):
        super().__init__(f'У вас недостаточно денег')

class NotEnoughChips(Exception):
    def __init__(self):
        super().__init__(f'У вас недостаточно фишек для продажи')

class StavkaError(Exception):
    def __init__(self):
        super().__init__(f'Введена некорректная ставка')