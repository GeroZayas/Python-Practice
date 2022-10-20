from prettytable import PrettyTable

pt = PrettyTable()

pt.field_names = ["name", "profession", "age", "comments"]

names = ["Gero", "Mar", "Elisa"]
professions = ["Python Programmer", "HHRR", "Doctor"]
ages = [31, 31, 56]
comments = [
    "This guy is amazing",
    "This is my girlfriend and I love her",
    "This is my mother and she's literally the best",
]

for name, profession, age, comment in zip(names, professions, ages, comments):
    pt.add_row([name, profession, age, comment])

print(pt)
