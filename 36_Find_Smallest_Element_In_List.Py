my_list = [
    "Palabras locas",
    "Gero",
    "Retozamiento fuerte",
    "Zayas",
    "Alvarez",
    "Alvaricoke",
]
print(my_list)

print("----------------")

for element in my_list:
    print(len(element))

print("----------------")


sorted_list = sorted(my_list, key=len)

print(sorted_list)

print("----------------")

second_smallest_element = sorted_list[1]

print(second_smallest_element)
