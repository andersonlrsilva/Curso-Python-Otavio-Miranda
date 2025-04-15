
from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

    def __len__(self):
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, valor):
        self._data[index] = valor

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':

    lista = MyList()
    lista.append('Maria')
    lista.append('Luiz')
    lista.append('Carlos')
    # print(lista._data)
    # print(len(lista))
    # print(lista[1])
    # lista[2] = "anderson"
    # print(lista._data)
    for iten in lista:
        print(iten)
