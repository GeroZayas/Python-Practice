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
