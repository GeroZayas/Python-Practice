import collections

nt = collections.namedtuple

people = nt("People", ["name", "age", "job"])

print(people)
