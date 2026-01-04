from rich import print

def remove_falsy(unfiltered_list):
    return list(filter(bool, unfiltered_list)) 

my_list = ["hello", "my", 0, 0, 1, False, True, "name", "is", "", "", "", "you", "know"]

print(my_list)

print(remove_falsy(my_list))