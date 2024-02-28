import heapq

my_array = [3, 6, 5, 2, 8, 1, 9, 10]


def separator():
    print("=" * 80)

# This is a comment

separator()
print(dir(heapq))
separator()

heapq.heapify(my_array)

print(my_array)
heapq.heappop(my_array)
print(my_array)

print(f"The 2 nmallest are {heapq.nsmallest(2, my_array)}")
print(f"The 2 nlargest are {heapq.nlargest(2, my_array)}")

# ---------------------- SECOND PRACTICE --------------------------

numbers = [2, 1, 23, 5, 11, 24]

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