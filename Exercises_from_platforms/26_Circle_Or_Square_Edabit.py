"""
Circle or Square
Publicado por Morgan Moore

Given the radius of a circle and the area of a square, return True if the circumference of the circle is greater than the square's perimeter and False if the square's perimeter is greater than the circumference of the circle.

Examples
circle_or_square(16, 625) ➞ True

circle_or_square(5, 100) ➞ False

circle_or_square(8, 144) ➞ True

Notes
You can use Pi to 2 decimal places (3.14).
Circumference of a circle equals 2 * Pi * radius.
To find the perimeter of a square using its area, find the square root of area (to get side length) and multiply that by 4.
"""


def circle_or_square(rad, area):
    pi = 3.14
    circumference = 2 * pi * rad
    square_area = (area**0.5) * 4
    return True if circumference > square_area else False


print(circle_or_square(16, 625))
print(circle_or_square(5, 100))
print(circle_or_square(8, 144))
