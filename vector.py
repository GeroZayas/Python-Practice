class Vector:
    def __init__(self) -> None:
        self._data = []  # create a list for def funcname(self, parameter_list):

    def append(self, value):
        self._data.append(value)

    def remove(self, index):
        del self._data[index]

    def insert(self, index, value):
        self._data.insert(index, value)

    def get(self, index):
        return self._data[index]

    def size(self):
        return len(self._data)
