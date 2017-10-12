# Evan Douglass
# Ch 2 Exercises: Miles-per-gallon

# This program calculates miles per gallon for a user's car

# input miles driven
miles = float(input('How many miles did you drive (no commas)? '))

# input gallons of gas used
gallons = float(input('How many gallons of gas did you use (no commas)? '))

# calculate miles per gallon
mpg = miles / gallons

# display result
print('Your car gets an average of', format(mpg, ',.2f'), 'miles per gallon.')
