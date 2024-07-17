import collections

nt = collections.namedtuple

people = nt("People", ["name", "age", "job"])

# print(people)

gero = people("Gero", 33, "Programmer")

print(gero.name)
print(gero.age)
print(gero.job)
