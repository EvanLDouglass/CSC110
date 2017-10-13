# Evan Douglass
# Learning Activity 6: Loops
# Grade at Plus

# This program counts from 1 to 120 by 17s using different control structures

# Main function
# No variables
# Calls the different counting functions
def main():
    while_loop()
    for_loop_w_list()
    for_loop_w_range()
    for_loop_w_range_single()

# While loop function
# No variables
# Counts to 120 by 17s using a while loop
def while_loop():
    # print heading
    print('Using the while loop:')
    # find values and print them
    value = 1
    print(value, end='')
    while value < 120:
        value += 17
        print(',', end=' ')
        print(value, end='')
    print()
    print()
    
# For loop function
# No variables
# Counts to 120 by 17s using a for loop
def for_loop_w_list():
    # print heading
    print('Using the for loop with a list:')
    # find values and print them
    print(1, end='')
    for value in [18, 35, 52, 69, 86, 103, 120]:
        print(',', end=' ')
        print(value, end='')
    print()
    print()

# For loop with range function
# No variables
# Counts to 120 by 17s using a for loop and the range function
def for_loop_w_range():
    # print heading
    print('Using the for loop with range:')
    # find values and print them
    print(1, end='')
    for value in range(18, 121, 17):
        print(',', end=' ')
        print(value, end='')
    print()
    print()

# For loop with range function and a single argument
# No variables
# Counts to 120 by 17s using a for loop and the range function with a single
# argument
def for_loop_w_range_single():
    # print heading
    print('Using the for loop with range, one argument:')
    # find values and print them
    print(1, end='')
    for value in range(7):
        print(',', end=' ')
        print((value + 1) * 17 + 1, end='')

# Call main
main()
