# Evan Douglass
# Lab 6: Geometric Functions
# Grade at plus

# This program creates functions to determine the area and perimeter of various
# shapes and calls them with a main function.

# Import math library
import math

# Main function
# Parameter: none 
# Returns: several statements about geometric values 
def main():
    print('A square of side 4.5 has area', square_area(4.5),
          'and perimeter', square_perimeter(4.5))

    print('A 4x5 rectangle has area', rectangle_area(4, 5),
          'and perimeter', rectangle_perimeter(4, 5))

    print('A circle of diameter 3 has area', circle_area(3),
          'and circumference', circle_perimeter(3))

    print('A right triangle with sides 4 and 5 has area', rt_triangle_area(4, 5),
          'and perimeter', rt_triangle_perimeter(4, 5))

    print('An equilaterial triangle of side 3.5 has area', eq_triangle_area(4.5),
          'and perimeter', eq_triangle_perimeter(4.5))

    print('An isosceles triangle with base 6 and height 4 has area',
          is_triangle_area(6, 4), 'and perimeter', is_triangle_perimeter(6, 4))

# Calculate area of a square
# Parameter: length of one side of the square
# Returns: area of a square
def square_area(side):
    return format(side ** 2, ',.3f')

# Calculate perimeter of a square
# Parameter: length of one side of the square
# Returns: perimeter of a square
def square_perimeter(side):
    return format(4 * side, ',.3f')

# Calculate area of a rectangle
# Parameters: the length and width of the rectangle
# Returns: area of the rectangle
def rectangle_area(width, height):
    return format(width * height, ',.3f')

# Calculate perimeter of a rectangle
# Parameters: the length and width of the rectangle
# Returns: perimeter of the rectangle
def rectangle_perimeter(width, height):
    return format(2 * (width + height), ',.3f')

# Calculate area of a circle
# Parameter: diameter of the circle
# Returns: area of the circle
def circle_area(diameter):
    return format(math.pi * (diameter / 2) ** 2, ',.3f')

# Calculate perimeter of a circle
# Parameter: diameter of the circle
# Returns: perimeter of the circle
def circle_perimeter(diameter):
    return format(math.pi * diameter, ',.3f')

# Calculate area of a right triangle
# Parameters: the two legs of the triangle that are not the hypotenuse
# Returns: the area of the right triangle
def rt_triangle_area(leg1, leg2):
    return format(0.5 * leg1 * leg2, ',.3f')

# Calculate area of a right triangle
# Parameters: the two legs of the triangle that are not the hypotenuse
# Returns: the area of the right triangle
def rt_triangle_perimeter(leg1, leg2):
    return format(leg1 + leg2 + math.sqrt(leg1 ** 2 + leg2 ** 2), ',.3f')

# Calculate area of an equilateral triangle
# Parameters: the side length of the triangle
# Returns: the area of the equilateral triangle
def eq_triangle_area(side):
    height = math.sqrt(side ** 2 + (0.5 * side) ** 2)
    return format(0.5 * side * height, ',.3f')

# Calculate perimeter of an equilateral triangle
# Parameters: the side length of the triangle
# Returns: the perimeter of the equilateral triangle
def eq_triangle_perimeter(side):
    return format(side * 3, ',.3f')

# Calculate area of an isoceles triangle
# Parameters: the base length and hight of the triangle
# Returns: the area of the isoceles triangle
def is_triangle_area(base, height):
    return format(base * height, ',.3f')

# Calculate perimeter of an isoceles triangle
# Parameters: the base length and hight of the triangle
# Returns: the perimeter of the isoceles triangle
def is_triangle_perimeter(base, height):
    return format((2 * math.sqrt((0.5 * base) ** 2 + height ** 2)) + base, ',.3f')

# Call main function
main()
