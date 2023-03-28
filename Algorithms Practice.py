# Numbers array

numbers = [5,4,7,6,9,2,1, 3, 8]

print("\nThis is our array of numbers:\n")
print(numbers)

# Insertion Sort
def insertion_sort(nums:list)->list:
	if len(nums) <= 1:
		return nums

	sorted_nums = []
	for num in nums:
		for i in range(len(sorted_nums)):
			if num < sorted_nums[i]:
				sorted_nums.insert(i, num)
				break
		else:
			sorted_nums.append(num)


	return sorted_nums


print("\nInsertion sort:", insertion_sort(numbers))


# Quick Sort
def quick_sort(nums:list)->list:
	if len(nums) <=1:
		return nums
	pivot = nums[0]
	left = []
	right = []
	for num in nums[1:]:
		if num < pivot:
			left.append(num)
		else:
			right.append(num)
	return quick_sort(left) + [pivot] + quick_sort(right)

		

print("\nQuick sort:", quick_sort(numbers))

# Merge Sort
def merge_sort(nums:list)->list:
	if len(nums) <=1:
		return nums

	mid = len(nums) // 2
	left = nums[:mid]
	right = nums[mid:]

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

def merge(left, right):
	sorted_arr = []
	left_index = right_index = 0
	while left_index < len(left) and right_index < len(right):
		l_e = left[left_index]
		r_e = right[right_index]
		
		if l_e < r_e:
			sorted_arr.append(l_e)
			left_index += 1
		else:
			sorted_arr.append(r_e)
			right_index += 1
	sorted_arr += left[left_index:]
	sorted_arr += right[right_index:]

	return sorted_arr

print("\nMerge sort:", merge_sort(numbers))


# Selection Sort
def selection_sort(nums:list):
	if len(nums) <=1:
		return nums
	min_index = 0

	for i in range(min_index+1, len(nums)):
		if nums[i] < nums[min_index]:
			min_index = i
	nums[0], nums[min_index] = nums[min_index], nums[0]

	return [nums[0]] + selection_sort(nums[1:])

print("\nSelection sort:", selection_sort(numbers))


# Binary Search Sort
