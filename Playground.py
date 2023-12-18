import collections

fullname = collections.namedtuple(
    typename='Full_name', field_names=['name', 'lastname']
)

gero_zayas = fullname("Gero", "Zayas")
print(gero_zayas.name, gero_zayas.lastname)