# Very simple program to practice with lists
# We are looking for the second smallest element in a given list

my_list = [
    "PalabrasLocas",
    "Bro",
    "RetozamientoFuerte",
    "Sambumba",
    "Locuraemocional",
    "Alvaricoke",
]

print(my_list)

# If we want to check the length our every element
for element in my_list:
    print(len(element))

# We sort the list and save it into another var "sorted_list"
# NOTE how we use the key=len argument for the sorted function
sorted_list = sorted(my_list, key=len)

print(sorted_list)

# We use index 1 to get hold of the second smallest element in our list
second_smallest_element = sorted_list[1]

print(second_smallest_element)

