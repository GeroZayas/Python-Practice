import sys
import timeit


my_tuple = (
    "Gero",
    31,
    "Barcelona",
)  # the parentheses are optional, if you take it away, it is still a tuple

print(my_tuple)

print("\n" + "*" * 25)  # LINE BREAK


# ----------------------------------------------------
# TUPLES are INMUTABLE you can not change items like in a list
# this means it can be more efficient sometimes, especially working with large data

# make a tuple from a list using tuple()

my_tuple_b = tuple(["Enrique", 54, "Holguin"])

print(my_tuple_b)
print(type(my_tuple_b))  # <class 'tuple'>

item = my_tuple[0]
print(item)  # Gero

print("\n" + "*" * 25)  # LINE BREAK

# ----------------------------------------------------

for i in my_tuple:
    print(i)

print("\n" + "*" * 25)  # LINE BREAK


# ----------------------------------------------------
if "Gero" in my_tuple:
    print("Yes")
else:
    print("No")

print("\n" + "*" * 25)  # LINE BREAK


# ----------------------------------------------------
print(len(my_tuple))  # 3

print("\n" + "*" * 25)  # LINE BREAK


# ----------------------------------------------------
# we can count how many times an item is in a tuple with .count()

my_letter_tuple = ("a", "b", "a", "c", "a")

print(my_letter_tuple)
print(my_letter_tuple.count("a"))  # 3

print("\n" + "*" * 25)  # LINE BREAK


# ----------------------------------------------------
# Make a list from a tuple with list()


my_letter_list = list(my_letter_tuple)
print(my_letter_list)  # ['a', 'b', 'a', 'c', 'a']

print("\n" + "*" * 25)  # LINE BREAK


# ----------------------------------------------------
# Compare lists and tuples
# sys is imported for this


print(sys.getsizeof(my_letter_tuple), "bytes")  # 80 bytes
print(sys.getsizeof(my_letter_list), "bytes")  # 96 bytes

print("\n" + "*" * 25)  # LINE BREAK


# ----------------------------------------------------
# it can be more efficient to iterate over a tuple
# we import timeit to compare

print("\n" + "*" * 25)  # LINE BREAK

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))  # 0.1059750679996796
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))  # 0.02168168599746423

# it takes longer to create the list than the tuple

# ----------------------------------------------------
# it can be more efficient to iterate over a tuple
# we import timeit to compare

print("\n" + "*" * 25)  # LINE BREAK
