import heapq

numbers = [4, 2, 7, 1, 9, 5]

heapq._heapify_max(numbers)

print(numbers)

max_num = heapq._heappop_max(numbers)

print(max_num)
print(numbers)

heapq._heapreplace_max(numbers, 3)

print(numbers)