# Evan Douglass
# Ch 3: Day of the Week

# This program asks for a number that will correspond to a day of the week

# Input number
day = int(input('Enter a number between 1 and 7: '))

# Output error message if number not in range 1-7
while day not in [1, 2, 3, 4, 5, 6, 7]:
    print('That is not a valid response, try again: ')
    print()
    day = int(input('Enter a number between 1 and 7: '))

# Output day of the week
if day == 1:
    print('That corresponds to Monday')
elif day == 2:
    print('That corresponds to Tuesday')
elif day == 3:
    print('That corresponds to Wednesday')
elif day == 4:
    print('That corresponds to Thursday')
elif day == 5:
    print('That corresponds to Friday')
elif day == 6:
    print('That corresponds to Saturday')
elif day == 7:
    print('That corresponds to Sunday')
