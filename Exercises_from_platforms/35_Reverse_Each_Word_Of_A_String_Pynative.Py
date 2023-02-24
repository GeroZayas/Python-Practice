"""
Reverse each word of a string
https://pynative.com/python-exercises-with-solutions/
"""

my_string = "My Name is Gero"

words = [word for word in my_string.split()]
reverse_words = ""

for word in words:
    reverse_words += word[::-1] + " "

print(reverse_words)
