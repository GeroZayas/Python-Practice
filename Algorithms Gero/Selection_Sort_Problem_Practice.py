from random import randint

numbers = [29, 24, 11, 27, 27, 2, 24, 28, 17]

print(f"\n\nThis is the array of numbers\n\n{numbers}\n\n")

"""
Problem: Given a list of n integers, 
write a Python function to find the kth smallest element 
in the list using selection sort algorithm.

The function should take the list and k as
inputs and return the kth smallest element.

Note that the kth smallest element is the kth element when the list is sorted in ascending order.
In the problem I provided, k represents the position of 
the element you want to find in the sorted list. 
For example, if k = 1, you want to find the smallest element in the list. 
If k = 2, you want to find the second smallest element in the list, and so on.

"""


def find_kth_smallest_element(nums, k=1):
    # Selection Sort implementation
    def selection_sort(arr):
        if len(arr) <= 1:
            return arr
        min_index = 0

        for i in range(min_index + 1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i

        arr[0], arr[min_index] = arr[min_index], arr[0]

        return [arr[0]] + selection_sort(arr[1:])

    sorted_nums = selection_sort(nums)
    print("""
	This is sorted_nums: 
	""")
    print(sorted_nums)

    endings = ["st", "nd", "rd", "th"]
    ending = str()
    if k == 1:
        ending = endings[0]
    elif k == 2:
        ending = endings[1]
    elif k == 3:
        ending = endings[2]
    else:
        ending = endings[3]

    return f"""
	The {k}{ending} smallest element is {sorted_nums[k-1]}
	"""


kth_element = randint(1, len(numbers))


r = find_kth_smallest_element(numbers, kth_element)

print(r)
