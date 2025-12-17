from src.errors import NoChipError


class CasinoBalance:

    def __init__(self, dct=None):
        if dct is None or not(isinstance(dct, dict)):
            raise NoChipError
        self.dct = dct

    def __len__(self):
        return len(self.dct)

    def __getitem__(self, key):
        if key not in self.dct.keys():
            raise IndexError
        else:
            return self.dct[key]

    def __setitem__(self, key, value):
        self.dct[key] = value

    def delete(self, key):
        if key in self.dct.keys():
            del self.dct[key]
        else:
            raise IndexError


