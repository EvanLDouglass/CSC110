# Evan Douglass
# HW: Children's Song, the Reprise
# Grade at challenge

# This program prints out several verses to the children's song "There was an
# Old Lady".

# main function
# prints the title and calls the verse functions
def main():
    # title
    print('There was an Old Lady')
    print()
    # fly verse
    verse1()
    # spider verse
    verse2()
    # bird verse
    verse3()
    # cat verse
    verse4()
    # dog verse
    verse5()
    # new verse
    verse6()
    # final verse
    lastverse()

# first verse function
# no variables
# prints out fly verse
def verse1():
    first_line('fly.')
    last_two()
    print()

# second verse function
# no variables
# prints out spider verse
def verse2():
    first_line('spider,')
    last_four()
    print()

# third verse function
# no variables
# prints out bird verse
def verse3():
    first_line('bird.')
    print('How absurd to swallow a bird.')
    extra('bird', 'spider,')
    last_four()
    print()

# fourth verse function
# no variables
# prints out cat verse
def verse4():
    first_line('cat.')
    print('Imagine that to swallow a cat.')
    extra('cat', 'bird.')
    extra('bird', 'spider,')
    last_four()
    print()

# fifth verse function
# no variables
# prints out dog verse
def verse5():
    first_line('dog.')
    print('My, what a hog, to swallow a dog.')
    extra('dog', 'cat.')
    extra('cat', 'bird.')
    extra('bird', 'spider,')
    last_four()
    print()

# sixth verse function
# no variables
# prints out a novel verse
def verse6():
    first_line('lynx.')
    print('She\'s big as the Sphinx if she swallowed a lynx.')
    extra('lynx', 'dog.')
    extra('dog', 'cat.')
    extra('cat', 'bird.')
    extra('bird', 'spider,')
    last_four()
    print()

# final verse function
# no variables
# prints out horse verse
def lastverse():
    first_line('horse.')
    print('She\'s dead, of course.')

# last 2 lines function
# no variables
# prints out the last two lines of each verse
def last_two():
    print('I don\'t know why she swallowed the fly.')
    print('Perhaps she\'ll die.')

# last 4 lines function
# no variables
# prints out last 4 lines of each verse
def last_four():
    print('That wriggled and jiggled and tickled inside her.')
    print('She swallowed the spider to catch the fly.')
    last_two()

# extra lines function
# variables: the animal swallowed and the animal it was meant to catch
# prints out the middle lines in each verse
def extra(animal1, animal2):
    print('She swallowed the', animal1, 'to catch the', animal2)

# first line function
# variable: animal swallowed
# prints out first line of each verse
def first_line(animal):
    print('There was an old lady who swallowed a', animal)

# call main
main()
