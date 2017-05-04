import time

class LinkedSparseArray:
    def __init__(self,n):
        self._n = n
        self._array = [None] * self._n

    def __len__(self):
        return self._n

    def __getitem__(self, j):
        if not -1 <= j < self._n:
            raise IndexError('Invalid index')
        elif j == -1:
            return self._array[self._n - 1]
        return self._array[j]

    def get_usage(self):
        counter = 0
        for i in self._array:
            if i is not None:
                counter += 1
        return counter

    def __setitem__(self, j, e):
        if not -1 <= j < self._n:
            raise IndexError('Invalid Index')
        elif j == -1:
            self._array[self._n - 1] = e
        self._array[j] = e


if __name__ == "__main__":
    start = time.time()
    l = LinkedSparseArray(10 ** 9)
    print("Get usage")
    print(l.get_usage())
    print("Setting Item....")
    l.__setitem__(0, 1)
    print("Done!")
    print("Getting item")
    print(l.__getitem__(0))
    print("Updated get_usage is")
    print(l.get_usage())
    print("Array Length is")
    print(l.__len__())
    print("Last item is")
    print(l.__getitem__(-1))
    end = time.time()
    print (end - start)
