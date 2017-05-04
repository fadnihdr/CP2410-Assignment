class LinkedSparseArray:
    def __init__(self):
        self._n = 10
        self._array = [None] * self._n

    def __len__(self):
        return self._n

    def __getitem__(self, j):
        if not 0 <= j < self._n:
            raise IndexError('Invalid index')
        else:
            if j == -1:
                return self._array[self._n - 1]
            return self._array[j]

    def get_usage(self):
        counter = 0
        for i in self._array:
            if i is None:
                counter += 1
        return counter

    def __setitem__(self, j, e):
        if not 0 <= j < self._n:
            raise IndexError('Invalid Index')
        self._array[j] = e


if __name__ == "__main__":
    l = LinkedSparseArray()
    print(l.get_usage())
    l.__setitem__(0, 1)
    print(l.__getitem__(0))
    print(l.__len__())
