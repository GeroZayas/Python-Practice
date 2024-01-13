from sys import getsizeof

# we create a list and then check the size of it
my_list = "Gero Mar Elisa Enrique Migdalia Sonia".split()

print(f"This is my list\n{my_list}")
print("This is the size of my_list")
print(getsizeof(my_list))  # 152

# now we append two more names to the list to
# see how it changes
my_list.extend("Basilio Zayas".split())

print(f"This is my list now\n{my_list}")
print("This is the size of my_list now")
print(getsizeof(my_list))  # the same 152

# we add more names now
my_list.extend("Karla Carly Carlos Tania Gissi Eduardito Vero".split())

print(f"This is my list now\n{my_list}")
print("This is the size of my_list now")
print(getsizeof(my_list))  # 184 -> it grew
