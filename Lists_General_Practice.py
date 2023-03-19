mylist1 = [1, "gero", 5.6, "zayas"]
print(mylist1)

# ------------------------------------------------

# I CREATE an empty list here ->
mylist2 = list()

print(mylist2)  # []

print(type(mylist2))  # <class 'list'>


# ------------------------------------------------

# ACCESS items from mylist1
item1, item2, item3, item4 = mylist1[0], mylist1[1], mylist1[2], mylist1[3]

print(item1)
print(item2)
print(item3)
print(item4)

print("*" * 20 + "\n")

for i, x in enumerate(mylist1):
    print(mylist1[i])

print("*" * 20 + "\n")

# ------------------------------------------------

# APPEND items to list

mylist2.append("name")
mylist2.append("job")
mylist2.append("nationality")

print("\n", mylist2)

# ------------------------------------------------

# INSERT items to list
mylist2.insert(1, "language")

print("\n", mylist2)

# ------------------------------------------------

# POP item from list

item = mylist2.pop()

print("\n", item)
print("\n", mylist2)

# ------------------------------------------------

# REMOVE item from list

item = mylist2.remove("name")

print("\n", mylist2)

# ------------------------------------------------

# REMOVE ALL ITEMS from list

item = mylist2.clear()

print("\n", mylist2)

# ------------------------------------------------

# REVERSE  items in list

mylist2 = ["superman", "spiderman", "batman", "aquaman"]

print("\n", mylist2)

item = mylist2.reverse()

print("\n", mylist2)

# ------------------------------------------------

# SORT  items in a list

number_list = [9, 4, 6, 2, 8, 5, 3]
print("\n", number_list)


# the .sort() method changes the original list
# number_list.sort()

# for a new list, without changing the original, we use sorted()


sorted_numbers_list = sorted(number_list)

print("\n", sorted_numbers_list)

# ------------------------------------------------
# PUT Two lists together

new_list = mylist1 + mylist2

print("\n", new_list)
print("the length of the new list is ", len(new_list))

# ------------------------------------------------
# SLICING

a_list = new_list[1:5]

b_list = new_list[::2]  # takes every two items

print("\n", a_list)
print("\n", b_list)

# ------------------------------------------------
# to do an actual copy of a list you have to use the .copy() method

c_list = a_list.copy() + ["hey"]

print("\n", a_list)  #  ['gero', 5.6, 'zayas', 'aquaman']
print("\n", c_list)  #  ['gero', 5.6, 'zayas', 'aquaman', 'hey']

print(len(a_list))  # 4
print(len(c_list))  # 5

# Another way to do a copy is to use list() and, as argument, the original list

animal_list = ["lion", "cat", "bird"]

animal_and_fruits_list = list(animal_list) + ["orange"] + ["lemon"]

print("\n", animal_list)
print("\n", animal_and_fruits_list)

# 3rd way to make a copy of a list -> SLICING [:] -> this means getting every item in the original list


animal_list = ["lion", "cat", "bird"]

animal_and_fruits_list = animal_list[:] + ["orange"] + ["lemon"]


print("\n", animal_list)
print("\n", animal_and_fruits_list)

# ------------------------------------------------
# list comprehension

# make a new list with square numbers from original list

print("\n", number_list)

square_numb_list = [i * i for i in number_list]

print("\n", square_numb_list)

new_numbers_list = [i for i in number_list] + [
    437
]  # this creates a copy of the original list and in this case i'm also adding another item -> 437

print("\n", new_numbers_list)
