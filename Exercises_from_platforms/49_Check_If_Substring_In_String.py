"""
https://www.w3resource.com/python-exercises/puzzles/index.php#EDITOR

5. Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings.

Input:
['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
Output:
True

Input:
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
Output:
False

Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
Output:
False

Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
Output:
True
"""


def check_substrings(string_list) -> bool:
    for string in string_list[:-1]:
        if (string) in string_list[-1]:
            return True
    return False


print(check_substrings(["a", "abb", "sfs", "oo", "de", "sfde"]))  # True

print(check_substrings(["a", "abb", "sfs", "oo", "ee", "sfde"]))  # False

print(
    check_substrings(
        ["a", "abb", "sad", "ooaaesdfe", "sfsdfde", "sfsd", "sfsdf", "qwrew"]
    )
)  # False

print(
    check_substrings(
        ["a", "abb", "sad", "ooaaesdfe", "sfsdfde", "sfsd", "sfsdf", "qwsfsdfrew"]
    )
)  # True
