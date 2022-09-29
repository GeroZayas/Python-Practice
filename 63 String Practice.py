# escaping backslash
my_string = 'I\' m  a "Geek"'
my_string = "I' m a 'Geek'"
print(my_string)

# backslash if you want to continue in the next line
my_string = "Hello \
World"
print(my_string)

# triple quotes for multiline strings
my_string = """
Hello
World
"""
print(my_string)


# ----- USEFUL METHODS -----
my_string = "     Hello World "

# remove white space
my_string = my_string.strip()
print(my_string)


# Upper and lower cases
print(my_string.upper())
print(my_string.lower())


# startswith and endswith
print("hello".startswith("he"))  # True
print("hello".endswith("llo"))  # True

# find first index of a given substring, -1 otherwise
print("Hello".find("o"))  # 4


# count number of characters/substrings
print("Hello".count("l"))  # 2


# replace a substring with another string (only if the substring is found)
# Note: The original string stays the same
message = "Hello World"
new_message = message.replace("World", "Universe")
print(new_message)

# SPLIT the string into a LIST
my_string = "how are you doing"
a = my_string.split()  # default argument is " "
print(a)  # ['how', 'are', 'you', 'doing']
my_string = "one,two,three"
a = my_string.split(",")
print(a)  # ['one', 'two', 'three']
