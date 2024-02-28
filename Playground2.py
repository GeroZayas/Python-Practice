import heapq
# from random import randint 

# numbers = [randint(1,30) for _ in range(6)]
numbers = [2, 1, 23, 5, 11, 24]


def separator():
    print("-" * 50)

print("Before heapify:")
print(numbers)

heapq.heapify(numbers)


separator()
print("After heapify Min Heap:")
print(numbers)

print("Popping from the Min Heap")
print(heapq.heappop(numbers))


separator()

print("Let's make it a MAx Heap")
numbers = [-n for n in numbers]
heapq.heapify(numbers)
numbers = [abs(n) for n in numbers]

print(numbers)

print("3 Largest numbers")
print(heapq.nlargest(3, numbers))
print("3 smallest numbers")
print(heapq.nsmallest(3, numbers))

print("Popping from the Max Heap")
print(heapq.heappop(numbers))