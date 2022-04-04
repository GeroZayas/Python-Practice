"""
The Vowel Code

Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
a -> 1
e -> 2
i -> 3
o -> 4
u -> 5

For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

"""


vowel_dict = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}


def encode(st):
    for letter in st:
        if letter in vowel_dict:
            st = st.replace(letter, str(vowel_dict[letter]))
    return st


def decode(st):
    for letter in st:
        for k, v in vowel_dict.items():
            if letter == str(v):
                st = st.replace(letter, k)
    return st


print(encode("hello"))
print(decode("h2ll4"))

print("------------------------------------------------------ 1")
# --------------------- Best Practices from CodeWars ---------------------


def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)


def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)


print(encode("Hi my name is Gero"))
print(decode("h2ll4"))
