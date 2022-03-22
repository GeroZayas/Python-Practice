# Remove duplicate characters in string

my_string = "Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library"

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
