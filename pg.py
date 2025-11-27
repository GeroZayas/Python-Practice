# memory_test.py
from memory_profiler import profile
from collections import namedtuple
from dataclasses import dataclass

@profile
def test_slots():
    class A:
        __slots__ = ('x', 'y')
        def __init__(self, x, y):
            self.x = x
            self.y = y
    return [A(1, 2) for _ in range(10_000)]

@profile
def test_dataclass():
    @dataclass
    class B:
        x: int
        y: int
    return [B(1, 2) for _ in range(10_000)]

@profile
def test_namedtuple():
    C = namedtuple('C', ['x', 'y'])
    return [C(1, 2) for _ in range(10_000)]

if __name__ == '__main__':
    print("Testing class with __slots__")
    test_slots()
    print("\nTesting dataclass")
    test_dataclass()
    print("\nTesting NamedTuple")
    test_namedtuple()