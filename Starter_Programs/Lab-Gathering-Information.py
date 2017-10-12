# Evan Douglass
# Lab 2: Gathering Information
# Grade at plus

# This program gathers the user's name and age then outputs this information
# in a greeting. It also displays the user's age in dog years and their age
# in one year.

# Input first and last name and age
first = input('What is your first name? ')
last = input('What is your last name? ')
age = int(input('What is your age? '))

# Calculate age in dog years
dog_age_1 = age * 7
# Calculate age next year
age_2 = age + 1
# Calculate dog year age next year
dog_age_2 = age_2 * 7

# Output initial greeting (name, initials, age)
print()
print("It's nice to meet you,", first, last + '.')
print('Your initials are', first[0] + last[0] + '.')
print("This year, you're", age, 'years old.')
# Output age in dog years
print("That's", str(dog_age_1) + ',', 'in "dog years".')
# Output age next year in human and dog years
print('Next year, you\'ll be', str(age_2) + ',', 'or', dog_age_2, 'in "dog years".')
