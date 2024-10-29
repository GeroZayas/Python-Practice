import collections

people = collections.namedtuple("People", "name job age")

gero = people("Gero", "Full Stack Programmer", 33)

for ele in gero:
    print(ele)
