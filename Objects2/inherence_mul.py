# Example of inherence
class SingleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, key):
        return self._items[key]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._items})"


class SortList(SingleList):
    def __init__(self, items=[]):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()


class IntList(SingleList):
    def __init__(self, items=[]):
        self._validate(items)
        super().__init__(items)

    def _validate(self, items):
        for item in items:
            if not isinstance(item, int):
                raise ValueError(f"The value given '{ item }' is not an integer.")

    def add(self, item):
        if isinstance(item, int):
            super().add(item)
        else:
            raise ValueError(f"The value given '{ item }' is not an integer.")


class OrderedIntList(IntList, SortList):
    pass


# Lista de enteros ordenada
int_ord_list = OrderedIntList([4, 5, 3, 1, 2])
print(int_ord_list)
int_ord_list.add(6)
print(int_ord_list)

# Cual es la primara clase padre
print(OrderedIntList.__base__)

# Cual es las clases padre
print(OrderedIntList.__bases__)

# MRO means method resolution order
print(OrderedIntList.__mro__)
