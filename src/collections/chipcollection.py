class ChipCollection:

    def __init__(self, lst=None):
        self.lst = list(lst) if lst is not None else []

    def add(self, item):
        self.lst.append(item)

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return ChipCollection(self.lst[key])
        else:
            return self.lst[key]

    def __iter__(self):
        for item in self.lst:
            yield item

    def pop(self, key):
        if key >= len(self.lst):
            raise IndexError
        else:
            self.lst.pop(key)

