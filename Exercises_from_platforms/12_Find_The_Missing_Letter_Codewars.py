"""
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter
in the array.

You will always get a valid array. And it will be always exactly one letter be missing. The length of the array will
always be at least 2. The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
"""

# upper and lowercase alphabets here:
lower_case_alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
upper_case_alpha = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def find_missing_letter(chars: list) -> str:
    # We declare the var that we will return, missing_letter:
    missing_letter = ""
    # we declare a var to later check and get hold of which list we are going to work with
    list_to_use = list
    # to determine with which list we are going to work (lower or upper case) we check the 1st char with the .isupper()
    # method
    if chars[0].isupper():
        list_to_use = upper_case_alpha
    else:
        list_to_use = lower_case_alpha
    # we get the range of the with which we are going to work, so we don't have to use the whole list
    index_first_letter = list_to_use.index(chars[0])
    index_last_letter = list_to_use.index(chars[-1])
    # we iterate through both lists and determine which element is different, missing in the given list 'chars'
    for element in list_to_use[index_first_letter:index_last_letter]:
        if element not in chars:
            missing_letter = element
    return missing_letter


print(find_missing_letter(["O", "Q", "R", "S"]))
print(find_missing_letter(["a", "b", "c", "d", "f"]))
