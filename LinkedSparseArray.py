import time


class LinkedSparseArray:
    def __init__(self, n):
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

    def fill(self,seq):
        if not 0 <= len(seq) < self._n:
            raise ValueError("Can't do that, fam")
        x = 0
        for i in seq:
            self._array[x] = i
            x =+ 1



if __name__ == "__main__":
    start = time.clock()
    list = [1,2,3,4,5,6,7,8]
    l = LinkedSparseArray(1000000)
    l.fill(list)
    end = time.clock()
    print(end - start)
