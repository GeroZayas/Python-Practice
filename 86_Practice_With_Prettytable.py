from prettytable import PrettyTable

pt = PrettyTable()

pt.field_names = ["name", "profession", "age"]

names = ["Gero", "Mar", "Elisa"]
professions = ["Python Programmer", "HHRR", "Doctor"]
ages = [31, 31, 56]

for name, profession, age in zip(names, professions, ages):
    pt.add_row([name, profession, age])

print(pt)
