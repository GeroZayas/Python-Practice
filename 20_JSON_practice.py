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

print(json.dumps(["apple", "bananas"]))  # list
print(json.dumps(("apple", "bananas")))  # tuple
print(json.dumps("hello"))  # string
print(json.dumps(42))  # int
print(json.dumps(31.76))  # float
print(json.dumps(True))  # boolean
print(json.dumps(False))  # boolean
print(json.dumps(None))  # None
