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


def camelCasing(txt: str) -> str:
    # Create a new string from the input str
    new_txt = ""
    # Substitute underscores for space in our new string
    # (so we can split it later without problem)
    for element in txt:
        # if the element is an underscore "_" we don't add it, instead a space
        if element == "_":
            new_txt += " "
        else:
            new_txt += element
    # Create a list of the words in our new string coming from
    # the input one
    str_splitted = new_txt.split()

    # in case the element is not from the alphabet we remove it
    # this way we eliminate spaces
    for element in str_splitted:
        if str(element).isalpha == False:
            str_splitted.remove(element)

    # Create our final_string list to be return as a str
    final_string = []
    for word in str_splitted:
        # Format thw 1st word in lower case
        if word == str_splitted[0]:
            final_string.append(word.lower())
        # The rest is capitalized
        else:
            final_string.append(word.title())

    return "".join(final_string)


print(camelCasing("snake_case"))  # snakeCase
print(camelCasing("Hello World"))  # helloWorld
print(camelCasing("tHe pRograMMer is HEre"))  # theProgrammerIsHere
