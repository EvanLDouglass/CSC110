# Evan Douglass
# Book checkpoint: 6.12

# This program writes the numbers 1-10 to a file

# open file
numbers = open('numbers.txt', 'w')

# for numbers 1-10:
for count in range(1, 11):
    # write number to file
    numbers.write(str(count) + '\n')
    
# close file
numbers.close()

# Display message
print('The numbers have been writen to numbers.txt')
