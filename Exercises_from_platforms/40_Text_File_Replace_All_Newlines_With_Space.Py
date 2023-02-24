"""
Exercise 2: Read text file into a variable and replace all newlines with space

Given: Assume you have a following text file (sample.txt).

Line1
line2
line3
line4
line5

Expected Output:

Line1 line2 line3 line4 line5

"""
with open("sample.txt", "r") as file:
    data = file.read().replace("\n", " ")
    print(data)
