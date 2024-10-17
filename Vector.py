class Vector:
    def __init__(self) -> None:
        self._data: list[int | float] = (
            []
        )  # create a list for def funcname(self, parameter_list):

    def append(self, value: float) -> None:
        self._data.append(value)

    def remove(self, index: int) -> None:
        del self._data[index]

    def insert(self, index: int, value: int | float) -> None:
        self._data.insert(index, value)

    def get(self, index: int) -> int | float:  # -> Any:
        return self._data[index]

    def size(self) -> int:
        return len(self._data)
