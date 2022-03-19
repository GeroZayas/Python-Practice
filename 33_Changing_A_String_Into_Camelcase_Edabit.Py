"""
Create a function that takes a string and returns it back in camelCase.

Examples

camelCasing("Hello World") ➞ "helloWorld"

camelCasing("snake_case") ➞ "snakeCase"

camelCasing("low high_HIGH") ➞ "lowHighHigh"

Notes

You need to remove all spaces and underscores.
There will be no numbers in inputs.

"""


from cgitb import text


def camelCasing(txt: str) -> str:
    new_txt = ""
    for element in txt:
        if element == "_":
            new_txt += " "
        else:
            new_txt += element

    print("this is new txt:", new_txt)
    str_splitted = new_txt.split()

    for element in str_splitted:
        if str(element).isalpha == False:
            str_splitted.remove(element)

    print(str_splitted)

    final_string = []
    for word in str_splitted:
        if word == str_splitted[0]:
            final_string.append(word.lower())
        else:
            final_string.append(word.title())

    return "".join(final_string)


print(camelCasing("snake_case"))  # snakeCase
print(camelCasing("Hello World"))  # helloWorld
