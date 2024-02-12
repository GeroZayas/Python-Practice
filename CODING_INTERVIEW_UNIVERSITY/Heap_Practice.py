import heapq

my_array = [3, 6, 5, 2, 8, 1, 9, 10]


def separator():
    print("=" * 80)


separator()
print(dir(heapq))
separator()

heapq.heapify(my_array)

print(my_array)
heapq.heappop(my_array)
print(my_array)
