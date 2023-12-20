import collections

fullname = collections.namedtuple(
    typename="Full_name", field_names=["name", "lastname"]
)

gero_zayas = fullname("Gero", "Zayas")
print(gero_zayas.name, gero_zayas.lastname)

print(fullname._fields)

# -------------------------------------------------

d = collections.deque([])

d.append("Gero")
d.append("Mar")
d.append(32)
d.extend(['Abuelo', 'Abuela', 45])
d.appendleft("Enrique")

print(d)
d.rotate(2)
print(d)

# -------------------------------------------------