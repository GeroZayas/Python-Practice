
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