"""
ROT13 is a simple letter substitution cipher that replaces a
letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered
with Rot13. If there are numbers or special characters included in the string,
they should be returned as they are.
Only letters from the latin/english alphabet should be shifted,
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


def rot13(message: str) -> str:
    low_alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'l',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                         'x',
                         'y', 'z']
    capital_alphabet_list = []
    for l in low_alphabet_list:
        capital_alphabet_list.append(l.upper())
    final_message = ''
    for letter in message:
        if letter in low_alphabet_list:
            the_index = low_alphabet_list.index(letter)
            rot_letter = low_alphabet_list[(the_index + 13) % 26]
            final_message += rot_letter
        elif letter in capital_alphabet_list:
            the_index = capital_alphabet_list.index(letter)
            rot_letter = capital_alphabet_list[(the_index + 13) % 26]
            final_message += rot_letter
        else:
            final_message += letter
    return final_message


print(rot13("test"))  # "grfg"
print(rot13("Test"))  # "Grfg"
