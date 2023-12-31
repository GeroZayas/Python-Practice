# my_str = "Gero is an amazing programmer and he really enjoys it"

# encoded_str = my_str.encode()

# print(encoded_str)
# print(type(encoded_str))
# print(type(my_str))

people = "Gero Mar Elisa Enrique Migdalia Sonia Basilio Zayas".split()
print(people)

people_iter = iter(people)
print(people_iter.__next__())
print(people_iter.__next__())
print(people_iter.__next__())
print(people_iter.__next__())
print(people_iter.__next__())
print(people_iter.__next__())
