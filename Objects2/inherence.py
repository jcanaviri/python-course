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
        return f'{self.__class__.__name__}({self._items})'

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
                raise ValueError('It is not an integer')

    def add(self, item):
        if isinstance(item, int):
            super().add(item)
        else:
            raise ValueError('It is not an integer')

single_list = SingleList([1, 2, 3])
print(single_list)

sort_list = SortList([9, 7, 8, 6, 1, 5, 4, 3, 2])
print(sort_list)
print(len(sort_list))

int_list = IntList([1, 2 ,3])
print(int_list)
