from collections import namedtuple
from types import SimpleNamespace

people = namedtuple("People", "name age job")

p1 = people("John", 25, "student")

p2 = people("Gero", 32, "programmer")

print(p1)
print(p2)

print(p1.name)
print(p1.job)

p3_props = ("Maca", 33, "HR")

p3 = people(p3_props[0], p3_props[1], p3_props[2])


print(p3.name, p3.job)


p4 = SimpleNamespace(name="Enrique", age=56, job="Teacher")

print(p4.name)
