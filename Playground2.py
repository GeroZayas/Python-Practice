from random import randint

def quicksort(arr):
	if len(arr) <= 1:
		return arr

	pivot = arr[0]

	left = []
	right = []

	for e in arr[1:]:
		if e < pivot:
			left.append(e)
		else:
			right.append(e)

	return quicksort(left) + [pivot] + quicksort(right)

# numbers = [randint(1,40) for _ in range(10)]

numbers = [29, 29, 9, 33, 5, 38, 13, 21, 11, 20]

print("This is numbers =>", numbers)

sorted_numbers = quicksort(numbers)

print("This is sorted_numbers =>", sorted_numbers)