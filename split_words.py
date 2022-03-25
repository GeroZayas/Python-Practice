"""
https://www.w3resource.com/python-exercises/puzzles/index.php#EDITOR
8. Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.

Input: W3resource Python, Exercises.

Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]

Input: The dance, held in the school gym, ended at midnight.

Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]

Input: The colors in my studyroom are blue, green, and yellow.

Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
"""
first_input = "W3resource Python, Exercises."
second_input = "The dance, held in the school gym, ended at midnight."
third_input = "The colors in my studyroom are blue, green, and yellow."

import re


# def split_words_separators(an_input: str) -> list:
#     """Returns two lists, one with words, and one with the separators used in input string"""
#     split_list = re.split(" |,", an_input)
#     words = []
#     separators = []
#     for element in split_list:
#         if str(element.isalpha()):
#             words.append(element)
#         else:
#             separators.append(element)
#     final_list_of_lists = [words, separators]
#     return final_list_of_lists


def split_words_separators(an_input: str) -> list:
    """Returns two lists, one with words, and one with the separators used in input string"""
    separators = []

    words = re.split(r"(\s)", an_input)
    # words = an_input.split("")
    for ele in words:
        for inside_ele in ele:
            if inside_ele in [" ", ","]:
                separators.append(inside_ele)
                ele.replace(inside_ele, "")
    # print(words)
    # print(separators)
    final_list = [words, separators]
    return final_list


print(split_words_separators(second_input))


# assert split_words_separators(second_input) == [
#     ["The", "dance", "held", "in", "the", "school", "gym", "ended", "at", "midnight."],
#     [" ", ", ", " ", " ", " ", " ", ", ", " ", " "],
# ], "different"
