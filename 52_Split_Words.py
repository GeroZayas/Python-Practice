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


def split_words_separators(an_input: str) -> list:
    """Returns two lists, one with words, and one with the separators used in input string"""
    merged = re.split(r"([ ,]+)", an_input)
    # the [::2] is to get the even indexes, which are the words
    # the [1::2] is to get the odd indexes, which are the separators
    return [merged[::2], merged[1::2]]


print("actual output")
print(split_words_separators(second_input))

print("-" * 60)

print("expected output")
expected_output = [
    ["The", "dance", "held", "in", "the", "school", "gym", "ended", "at", "midnight."],
    [" ", ", ", " ", " ", " ", " ", ", ", " ", " "],
]
print(expected_output)
