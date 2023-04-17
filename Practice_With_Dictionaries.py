my_dict = {"name": "Gero", "age": 31, "city": "Barcelona"}

print(my_dict)

# ----- ANOTHER WAY To CREATE A DICT -----

my_dict2 = dict(name="Rafa", age=18, city="Holguin")

print(my_dict2)

# ----- Get Value from DICT -----

value = my_dict["name"]
print(value)  # Gero

value = my_dict2["name"]
print(value)  # Rafa

# ----- Change Item in DICT -----
my_dict["name"] = "Tigre Tropical Caliente"
print(my_dict)

# ----- DELETE Item in DICT -----

# del
del my_dict["name"]
print(my_dict)


# .pop()
my_dict.pop("age")
print(my_dict)

# .popitem() -> This removes the last inserted item

print(my_dict2)

my_dict2.popitem()

print(my_dict2)

# ----- CHECK Item in DICT -----
if "lastname" in my_dict2:
    print(my_dict2["name"])
else:
    print("NOT FOUND")

# another way
try:
    print(my_dict2["lastname"])
except:
    print("ERROR. NOT FOUND")

# ----- LOOP through in DICT -----

# to get the keys
for key in my_dict2:
    print(key)

# to get the values
for value in my_dict2.values():
    print(value)

# to get the keys and the values
for key, value in my_dict2.items():
    print(key, value)

# ----- To MAKE an ACTUAL COPY of a DICT -----
my_dict3 = my_dict.copy()
print(my_dict3)

my_dict3["love"] = "Mar"
my_dict3["passion"] = "programming"

print(my_dict3)


# Another way -> use dict()

my_dict4 = dict(my_dict3)

my_dict4["city"] = "Sidney"
print(my_dict4)


# ----- To UPDATE a DICT -----
new_dict = {"Name": "Fernando", "age": 100, "job": "policeman"}
print(new_dict)

new_dict_2 = {"Name": "Julio", "age": 84, "job": "policeman", "money": 120000}

# we update the new_dict
new_dict.update(new_dict_2)
print(new_dict)
