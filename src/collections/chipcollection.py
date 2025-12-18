from src.objects.chip import Chip


class ChipCollection:

    def __init__(self, lst: list | None =None):
        """
        Инициализация коллекции фишек
        :param lst: список с фишками
        """
        self.lst = list(lst) if lst is not None else []

    def add(self, item: Chip):
        """
        Добавление фишки в коллекцию
        :param item: фишка
        """
        self.lst.append(item)


    def __len__(self) -> int:
        """
        Функция для подсчета длины коллекции
        :return: длину коллекции
        """
        return len(self.lst)

    def __getitem__(self, key: int | slice):
        """
        Функция для получения элемента по ключу или срезу
        :param key: срез или ключ
        :return: элемент или срез
        """
        if isinstance(key, slice):
            return ChipCollection(self.lst[key])
        else:
            return self.lst[key]

    def __setitem__(self, key: int, value: Chip):
        """
        Заменяет фишку в коллекции по индексу
        :param key: индекс вставки
        :param value: значение вставки
        """
        self.lst[key] = value

    def __iter__(self):
        """
        Функция для итерирования по коллекции
        """
        for item in self.lst:
            yield item

    def pop(self, key):
        """
        Фукнкция для удаления элемента коллекции по индексу
        :param key: индекс
        """
        if key >= len(self.lst):
            raise IndexError
        else:
            self.lst.pop(key)

    def __repr__(self):
        s = ""
        for i in range(len(self.lst)):
            s += f"{self.lst[i].stack} фишек цвета {self.lst[i].color} "
        return s

