from traceback import print_tb


my_tuple = (
    "Gero",
    31,
    "Barcelona",
)  # the parentheses are optional, if you take it away, it is still a tuple

print(my_tuple)

# ----------------------------------------------------
# TUPLES are INMUTABLE you can not change items like in a list
# this means it can be more efficient sometimes, especially working with large data

# make a tuple from a list using tuple()

my_tuple_b = tuple(["Enrique", 54, "Holguin"])

print(my_tuple_b)
print(type(my_tuple_b))  # <class 'tuple'>

item = my_tuple[0]
print(item)  # Gero

# ----------------------------------------------------

for i in my_tuple:
    print(i)

# ----------------------------------------------------
if "Gero" in my_tuple:
    print("Yes")
else:
    print("No")

# ----------------------------------------------------
print(len(my_tuple))  # 3

# ----------------------------------------------------
# we can count how many times an item is in a tuple with .count()

my_letter_tuple = ("a", "b", "a", "c", "a")

print(my_letter_tuple)
print(my_letter_tuple.count("a"))  # 3

# ----------------------------------------------------
# Make a list from a tuple with list()

my_letter_list = list(my_letter_tuple)
print(my_letter_list)  # ['a', 'b', 'a', 'c', 'a']

# ----------------------------------------------------
#
