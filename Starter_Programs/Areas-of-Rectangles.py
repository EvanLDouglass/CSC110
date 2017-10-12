# Evan Douglass
# Ch 3: Areas of Rectangles

# This program compares the areas of two rectangles with sides determined by
# user input.

# Get sides for rectangle 1
side1_1 = float(input('Side 1 of the first rectangle: '))
side2_1 = float(input('Side 2 of the first rectangle: '))
print()

# Calculate area of rect. 1
area1 = side1_1 * side2_1

# Get sides for rectangle 2
side1_2 = float(input('Side 1 of the second rectangle: '))
side2_2 = float(input('Side 2 of the second rectangle: '))
print()

# Calculate area of rect. 2
area2 = side1_2 * side2_2

# Output comparison of the two rectangles
if area1 < area2:
    print('area 1 < area 2')
elif area1 == area2:
    print('area 1 = area 2')
elif area1 > area2:
    print('area 1 > area 2')
