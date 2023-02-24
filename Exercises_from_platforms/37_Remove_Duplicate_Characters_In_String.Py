# Remove duplicate characters in string

my_string = "This guy is an amazing programmer"

print(my_string)

# We create a set so that we can eliminate duplicate characters
set_string = set(my_string)

print("\n", set_string)

# we declare a new string var
new_string = ""

# We add elements to the string var and avoid punctuation
# as we only want the alpha characters now
for ele in set_string:
    if ele not in [" ", ",", ".", "-"]:
        new_string += ele + " "


print("\n", new_string)

# We can check how many individual characters we have in this case
print("\nThe number of individual alpha characters is: ")
print("\n", len(new_string.replace(" ", "")))


# Another way to do it, keeping the order of characters
def remove_duplicate(string):
    result = ""
    for char in string:
        if char not in result and char != " ":
            result += char
    return result


print("\n")
print(remove_duplicate("This guy is an amazing programmer"))
