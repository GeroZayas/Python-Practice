

numbers = [7, 6, 5, 4, 3, 2, 1, 78, 32, 12,7,39, 65]

print("numbers: ", numbers)

###########################################################

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot  = arr[0]
	left = []
	right = []

	for e in arr[1:]:
		if e < pivot:
			left.append(e)
		else:
			right.append(e)

	return quicksort(left) + [pivot] + quicksort(right)

quicksort_result = quicksort(numbers)

print(quicksort_result)

###########################################################

def insertion_sort(arr):
	size = len(arr)
	if size <= 1:
		return size

	sorted_arr = []

	for ele in arr:
		for i in range(len(sorted_arr)):
			if ele < sorted_arr[i]:
				sorted_arr.insert(i, ele)
				break
		else:
			sorted_arr.append(ele)

	return sorted_arr

insertion_sort_result = insertion_sort(numbers)

print(insertion_sort_result)


print(quicksort_result == insertion_sort_result) # true

###########################################################

def merge_sort(arr:list)->list:
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)


def merge(left, right):
	sorted_arr = []
	left_index = right_index = 0

	while left_index < len(left) and right_index < len(right):
		if left[left_index] < right[right_index]:
			sorted_arr.append(left[left_index])
			left_index += 1
		else:
			sorted_arr.append(right[right_index])
			right_index += 1

	sorted_arr += left[left_index:]
	sorted_arr += right[right_index:]

	return sorted_arr

merge_sort_result = merge_sort(numbers)

print(merge_sort_result)
print(merge_sort_result == quicksort_result == insertion_sort_result)

###########################################################

def selection_sort(arr:list):
	if len(arr) <= 1:
		return arr
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_idx]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]

###########################################################

selection_sort(numbers) # sorted in-place

print(numbers)

###########################################################

def binary_search(arr, left, right, target):
	if left > right:
		return 'Element not found'

	mid = (left + right) // 2

	if target == arr[mid]:
		return f'Element found at index {mid}'
	elif target < arr[mid]:
		return binary_search(arr, left, mid - 1, target)
	else:
		return binary_search(arr, mid + 1, right, target)


print(binary_search(arr = numbers, left = 0, right = len(numbers), target = 32))

###########################################################

