from random import randint
from typing import List

numbers = [randint(1,100) for _ in range(10)]

print('numbers: ', numbers)

# ----------------------------------------------------------------

def quicksort(arr:List[int])-> List[int]:
    