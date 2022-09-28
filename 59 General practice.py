mylist1 = [1, "gero", 5.6, "zayas"]
print(mylist1)

# I create an empty list here ->
mylist2 = list()

print(mylist2)  # []

print(type(mylist2))  # <class 'list'>

# access items from mylist1
item1, item2, item3, item4 = mylist1[0], mylist1[1], mylist1[2], mylist1[3]

print(item1)
print(item2)
print(item3)
print(item4)

print("*" * 20 + "\n")

for i, x in enumerate(mylist1):
    print(mylist1[i])

print("*" * 20 + "\n")
