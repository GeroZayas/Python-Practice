"""
Stuttering Function
Publicado por Deep Xavier

Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

Examples
stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"
Notes
Assume all input is in lower case and at least two characters long.
"""


def stutter(word):
    first_two_letters = word[:2]
    final_string = (f"{first_two_letters}... " * 2) + word + "?"
    return final_string


print(stutter("outstanding"))
