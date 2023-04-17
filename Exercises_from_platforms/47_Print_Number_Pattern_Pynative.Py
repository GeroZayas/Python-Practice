"""
Exercise 7: Print the following number pattern
https://pynative.com/python-exercises-with-solutions/

Exercise 7: Print the following number pattern

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

"""
cnt = 5
for x in range(1, 6):
    print(f"{x } " * cnt)
    cnt -= 1
