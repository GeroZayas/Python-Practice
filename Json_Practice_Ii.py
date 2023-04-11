import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}

# convert into JSON:
person_json = json.dumps(person)


# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)


# the result is a JSON string:
print(person_json)
print(person_json2)

# with open("person.json", "w") as f:
#     json.dump(person, f)  # you can also specify indent etc...

# FROM JSON to Python (Deserialization, Decode)
"""Convert a JSON string into a Python object with the json.loads() method. The result will be a Python dictionary."""

person_json = """
{
    "age": 30, 
    "city": "New York",
    "hasChildren": false, 
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""

# makes it a dictionary
person = json.loads(person_json)
print(person)
