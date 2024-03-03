def square(x):
    return x ** 2

numbers = [1,2,3,4,5]

nums_squares = [square(num) for num in numbers]

print(nums_squares)

map_num_squares = list(map(square, numbers))

print(map_num_squares)