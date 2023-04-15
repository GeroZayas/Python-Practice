

numbers = [7, 6, 5, 4, 3, 2, 1, 78, 32, 12,7,39, 65]

print("numbers: ", numbers)

###########################################################

def quicksort(arr):
	...

quicksort_result = quicksort(numbers)

print(quicksort_result)

###########################################################

def insertion_sort(arr):
	...

insertion_sort_result = insertion_sort(numbers)

print(insertion_sort_result)


print(quicksort_result == insertion_sort_result) # true

###########################################################

def merge_sort(arr:list)->list:
	...


def merge(left, right):
	...

merge_sort_result = merge_sort(numbers)

print(merge_sort_result)
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

