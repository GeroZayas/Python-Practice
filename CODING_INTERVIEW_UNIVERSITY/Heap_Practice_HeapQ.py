import heapq

my_array = [3, 6, 5, 2, 8, 1, 9, 10]


def separator():
    print("=" * 80)

# This is a comment

separator()
print(dir(heapq))
separator()

print("\nHeapifying the array\n")
heapq.heapify(my_array)
print(my_array)


print("\nPopping from the array\n")
heapq.heappop(my_array)
print(my_array)

print(f"\nThe 2 nmallest are {heapq.nsmallest(2, my_array)}")
print(f"\nThe 2 nlargest are {heapq.nlargest(2, my_array)}")

# ---------------------- SECOND PRACTICE --------------------------

print()

separator()
print("SECOND PRACTICE")
separator()

numbers = [2, 1, 23, 5, 11, 24]

print("\nBefore heapify:\n")
print(numbers)

heapq.heapify(numbers)

print("\nAfter heapify Min Heap:\n")
print(numbers)

print("\nPopping from the Min Heap\n")
print(heapq.heappop(numbers))


print()

# ---------------------- MAX PRACTICE --------------------------

separator()
print("MAX HEAP PRACTICE")
separator()

print("\n\nLet's make it a MAx Heap\n\n")
numbers = [-n for n in numbers]
heapq.heapify(numbers)
numbers = [abs(n) for n in numbers]

print(numbers)

print("\n3 Largest numbers")
print(heapq.nlargest(3, numbers))
print("\n3 smallest numbers")
print(heapq.nsmallest(3, numbers))

print("\nPopping from the Max Heap")
print(heapq.heappop(numbers))


# ---------------------- MAX PRACTICE WITH PRIVATE METHODS --------------------------

separator()
print("MAX HEAP PRACTICE WITH PRIVATE METHODS")
separator()

print("\n\nLet's make it a MAx Heap\n\n")
numbers = [7,3,6,4,9,2,10,3]

heapq._heapify_max(numbers)

print(numbers)

print([])

