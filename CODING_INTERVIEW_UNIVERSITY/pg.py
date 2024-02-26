from heapq import heapify
from random import randint

heap = [randint(1, 30) for _ in range(20)]
print("Heap before heapify")
print(heap)

heapify(heap)

print("Heap after being heapified")
print(heap)
