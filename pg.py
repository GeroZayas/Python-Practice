from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'gender'])

# Create a new Person object
p = Person('Bob', 30, 'Male')

# Access the fields using dot notation
print(p.name)   # Output: 'Bob'
print(p.age)    # Output: 30
print(p.gender) # Output: 'Male'