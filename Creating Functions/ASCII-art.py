# Evan Douglass
# Learning Activity: ASCII Art
# Grade at plus

# This program uses functions to draw simple ASCII art

# Create a function to print a box
def box():
    print('+------+')
    print('|      |')
    print('|      |')
    print('|      |')
    print('+------+')

# Create a function to draw an up arrow head
def up_arrow():
    print(r'   /\   ')
    print(r'  /  \  ')
    print(r' /    \ ')

# Create a function to draw a down arrow head
def down_arrow():
    print(r' \    / ')
    print(r'  \  /  ')
    print(r'   \/   ')
    
# Create a function to print a diamond
def diamond():
    up_arrow()
    down_arrow()
    
# Create a function to print an X
def X():
    down_arrow()
    up_arrow()

# Create a function to print a rocket
def rocket():
    up_arrow()
    box()
    print('|United|')
    print('|States|')
    box()
    up_arrow()
    
# The main function
def main():
    # Call the function a couple times
    box()
    print()
    diamond()
    print()
    X()
    print()
    rocket()

# Call main function
main()
