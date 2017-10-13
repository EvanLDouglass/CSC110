# Evan Douglass
# HW 2: Fish Pond
# Grade at Challenge

# This program calculates and displays dimensions for various fish pond shapes.

import math

# Input type of pond
print('Fish ponds are available in the following shapes:\n'
      '\tcircle, square, rectangle, oval, L')
pond_type = input('Please select the shape for your fish pond: ')

# Output error message if input unrecognized
if pond_type != 'circle' and pond_type != 'square' and pond_type != 'rectangle' \
   and pond_type != 'oval' and pond_type != 'L':
    print()
    print('Unrecognized shape', '"' + pond_type + '".')
    print('Please run the program again.')
    # End Program
    raise SystemExit

# Input depth
print('Fish ponds are available in the following depths:\n'
      '\t18, 24, 30')
depth = input('Please select the depth for your fish pond: ')

# Output error message if input unrecognized
if depth != '18' and depth != '24' and depth != '30':
    print()
    print('Unrecognized depth', '"' + str(depth) + '".')
    print('Please run the program again.')
    # End Program
    raise SystemExit
# Convert depth to feet
else:
    depth = int(depth) / 12

# If pond is a circle
if pond_type == 'circle':
    # Calculate Surface Area (SA) and volume
    radius = 5/2
    base_area = math.pi * (radius ** 2)
    perim = 2 * math.pi * radius
    side_area = depth * perim
    surface_area = base_area + side_area
    volume = depth * base_area
    # Calculate border area
    border_radius = 9 / 2
    border_circle = math.pi * (border_radius ** 2)
    border_area = border_circle - base_area
# If pond is square
elif pond_type == 'square':
    # Calculate SA and volume
    length = 5
    width = 5
    base_area = length * width
    perim = 4 * length
    side_area = depth * perim
    surface_area = base_area + side_area
    volume = depth * base_area
    # Calculate border area
    b_length = 9
    border_square = b_length ** 2
    border_area = border_square - base_area
# If pond is rectangular
elif pond_type == 'rectangle':
    # Calculate SA and volume
    length = 7
    width = 4
    base_area = length * width
    perim = (2 * length) + (2 * width)
    side_area = depth * perim
    surface_area = base_area + side_area
    volume = depth * base_area
    # Calculate border area
    b_length = 11
    b_width = 8
    border_rectangle = b_length * b_width
    border_area = border_rectangle - base_area
# If pond is oval
elif pond_type == 'oval':
    # Dimentions
    width_rec = 2
    length_rec = 4
    radius_circ = 2
    # Base area
    base_area_rec = width_rec * length_rec
    base_area_circ = math.pi * (radius_circ ** 2)
    base_area = base_area_rec + base_area_circ
    # Perimeter
    base_per_rec = 2 * width_rec
    base_per_circ = 2 * math.pi * radius_circ
    perim = base_per_rec + base_per_circ
    # Side area
    side_area = depth * perim
    # SA and volume
    surface_area = base_area + side_area
    volume = depth * base_area
    # Calculate border area
    border_radius = 4
    border_length = 8
    border_width = 2
    border_area_circ = math.pi * (border_radius ** 2)
    border_area_rec = border_length * border_width
    border_area = (border_area_circ + border_area_rec) - base_area
# If pond is L shaped
elif pond_type == 'L':
    # Dimentions
    full_length = 10
    full_width = 6
    part_length = 5
    part_width = 3
    # Base Area
    full_area = full_length * full_width
    part_area = part_length * part_width
    base_area = full_area - part_area
    # Perimeter
    perim = full_length + (4 * part_width) + part_length
    # Side area
    side_area = depth * perim
    # SA and volume
    surface_area = base_area + side_area
    volume = depth * base_area
    # Calculate border area
    new_full_L = 14
    new_full_W = 10
    border_area = ((new_full_L * new_full_W) - part_area) - base_area

print()

# Output volume of selected pond
print('The volume of your fish pond is', format(volume, ',.3f'), 'cubic feet.')

# Output SA of selected pond
print('The surface area of your fish pond is', format(surface_area, ',.3f'),
      'square feet.')

# Output area of border
print('The area of the border is', format(border_area, ',.3f'), 'square feet.')
