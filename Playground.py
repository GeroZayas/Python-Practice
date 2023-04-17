
<<<<<<< HEAD
def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (nums[i], nums[j])
    return ()

arr = [8, 7, 2, 5, 3, 1]
target = 10

r = findPairs(arr, target)
print(r)


arr = [5, 2, 6, 8, 1, 9]
target = 12

r = findPairs(arr, target)
print(r)


arr = [1,1,1,1]
target = 2

r = findPairs(arr, target)
print(r)







=======

numbers = [7, 6, 5, 4, 3, 2, 1, 78, 32, 12,7,39, 65]

print("numbers: ", numbers)

###########################################################

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

quicksort_result = quicksort(numbers)

print("quicksort_result => ", quicksort_result)

###########################################################

def insertion_sort(arr):
	if len(arr) <= 1:
		return arr
	sorted_arr = []
	for elem in arr:
		for j in range(len(sorted_arr)):
			if elem < sorted_arr[j]:
				sorted_arr.insert(j, elem)
				break
		else:
			sorted_arr.append(elem)

	return sorted_arr

insertion_sort_result = insertion_sort(numbers)

print("insertion_sort_result => ", insertion_sort_result)

print("quicksort_result == insertion_sort_result", end= ' => ') # true

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
	i = j = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			sorted_arr.append(left[i])
			i += 1
		else:
			sorted_arr.append(right[j])
			j += 1

	sorted_arr += left[i:]
	sorted_arr += right[j:]

	return sorted_arr

merge_sort_result = merge_sort(numbers)

print("merge_sort_result => ", merge_sort_result)
print("merge_sort_result == quicksort_result == insertion_sort_result", end=' -> ')
print(merge_sort_result == quicksort_result == insertion_sort_result)

###########################################################

def selection_sort(arr:list):
	...

###########################################################

selection_sort(numbers) # sorted in-place

print(numbers)

###########################################################

def binary_search(arr, left, right, target):
	...


print(binary_search(arr = numbers, left = 0, right = len(numbers), target = 32))

###########################################################
>>>>>>> da9161e272ef04900ab3b001417c7e89b88cbd6f

