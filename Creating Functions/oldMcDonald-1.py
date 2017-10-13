# Evan Douglass
# HW: Children's Song
# Grade at challenge

# This program uses functions to output verses to the children's song "Old
# McDonald"

# Create main function to output song
# No parameters
# Calls title and verse functions as well as extra verses
def main():
    title()
    verse('chicken', 'cluck')
    verse('cow', 'moo')
    verse('duck', 'quack')
    newVerse()
    prompt = input('Do you want to have a fifth verse (yes/no)? ')
    if prompt != 'no':
        print()
        newVerse()
    else:
        raise SystemExit

# Create title function
# No parameters
# Outputs the song title and a blank line
def title():
    print('Old McDonald')
    print()

# Create helper function for verse function
# Parameters: a word
# Outputs "an" or "a" depending on the first letter of the animal name
def a_an(word):
    word = word.lower()
    if word[0] in 'aeiou':
        return 'an'
    else:
        return 'a'

# Create helper function for verse function
# No parameters
# Outputs the first and last line of the verse
def first_last():
    print('Old McDonald had a farm, E-I-E-I-O.')


# Create verse function
# Parameters: animal and the sound it makes
# Outputs a verse of the song using arguments provided
def verse(animal, sound):
    first_last()
    print('And on that farm he had', a_an(animal), animal + ',', 'E-I-E-I-O.')
    print('With', a_an(sound), sound + '-' + sound, 'here, and',
          a_an(sound), sound + '-' + sound, 'there.')
    print('Here', a_an(sound), sound + ',', 'there', a_an(sound),
          sound + ',','everywhere', a_an(sound), sound + '-' + sound + '.')
    first_last()
    print()

# Create new verse function
# Parameters: animal and sound it makes from user input
# Outputs a verse of the song using the arguments provided
def newVerse():
    animal = input('Enter an animal: ')
    sound = input('Enter the sound the {} makes: '.format(animal))
    print()
    verse(animal, sound)
    

main()
