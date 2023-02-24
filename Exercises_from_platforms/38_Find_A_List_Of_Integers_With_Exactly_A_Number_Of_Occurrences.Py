"""
1. Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. 

https://www.w3resource.com/python-exercises/puzzles/index.php#EDITOR
"""
first_input = [19, 19, 15, 5, 3, 5, 5, 2]
second_input = [19, 15, 15, 5, 3, 3, 5, 2]
third_input = [19, 19, 5, 5, 5, 5, 5]


def find_ocurrences(num: int, times: int, a_list: list) -> bool:
    counter = 0
    number = num
    for num in a_list:
        if num == number:
            counter += 1
    return True if counter >= times else False


print(
    "True"
    if find_ocurrences(num=19, times=2, a_list=first_input)
    and find_ocurrences(num=5, times=3, a_list=first_input)
    else "False"
)

print(
    "True"
    if find_ocurrences(num=19, times=2, a_list=second_input)
    and find_ocurrences(num=5, times=3, a_list=second_input)
    else "False"
)

print(
    "True"
    if find_ocurrences(num=19, times=2, a_list=third_input)
    and find_ocurrences(num=5, times=3, a_list=third_input)
    else "False"
)
