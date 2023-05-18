from random import randint

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[0]
	left = [x for x in arr[1:] if x < pivot]
	right = [x for x in arr[1:] if x >= pivot]

	return quicksort(left) + [pivot] + quicksort(right)

numbers = [randint(1,89) for _ in range(20)]
print(numbers)

res = quicksort(numbers)

print(res)