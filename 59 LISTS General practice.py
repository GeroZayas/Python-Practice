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
