import json

# a Python object (dict):
x = {
    "name": "Gero",
    "age": 30,
    "city": "Barcelona"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

print('*' * 60)

print(json.dumps(["apple", "bananas"]))  # list
print(json.dumps(("apple", "bananas")))  # tuple
print(json.dumps("hello"))  # string
print(json.dumps(42))  # int
print(json.dumps(31.76))  # float
print(json.dumps(True))  # boolean
print(json.dumps(False))  # boolean
print(json.dumps(None))  # None


print('*' * 60)

# Convert a Python object containing all the legal data types:

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

print('*' * 60)

# formatting the result
print(json.dumps(x, indent=4))

print('*' * 60)
