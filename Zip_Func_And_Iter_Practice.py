# use of the zip function to use for loop in multiple lists at once.
names = ["Sonia", "Basilio", "Elisabeth", "Rafa"]
part_family = ["Abuela", "Abuelo", "Mama", "Hermano"]
job = ["Housewife", "Locksmith", "Doctor", "Student"]

for name, relation, the_job in zip(names, part_family, job):
    print(f"{name} is {relation} and does the {the_job}")


print("-" * 15)

# This prints the tuple of all three of those values
for value in zip(names, part_family, job):
    print(list(value))

print("-" * 15)

# You can run it like this:
# i_names = names.__iter__()
# Or like this:
i_names = iter(names)


print(next(i_names))
print(next(i_names))
print(next(i_names))
