# Evan Douglass
# HW 8: Children's Songs, the Sequel
# Grade at challenge

'''The oldMcDonald module houses several functions that can be used to write
the children's song "Old McDonald"'''

SOUNDS = []
ANIMALS = []

# Title method
# No parameters
def title():
   'Outputs the song title and a blank line'
   print('Old McDonald')
   print()

# Verse method
# Parameters: animal and the sound it makes
def verse(animal, sound):
   'Outputs a verse of the song using arguments provided'
   first_last()
   print('And on that farm he had', a_an(animal), animal + ',', 'E-I-E-I-O.')
   SOUNDS.append(sound)
   ANIMALS.append(animal)
   # cycle through sounds already used
   for sound in SOUNDS[::-1]:
      print('With', a_an(sound), sound + '-' + sound, 'here, and',
            a_an(sound), sound + '-' + sound, 'there.')
      print('Here', a_an(sound), sound + ',', 'there', a_an(sound),
            sound + ',','everywhere', a_an(sound), sound + '-' + sound + '.')
   first_last()
   print()

# Ask for another verse method
# No Parameters
def query_verse():
   '''Asks the user for an animal and the sound it makes in order to output
a new verse. Five invalid tries will return False and terminate program.'''
   ready_a = False
   ready_s = False
   count_a = 0
   count_s = 0
   
   # ask for an animal
   animal = input('Enter an animal: ')
   # ensure valid entry and limit to 5 tries
   while not ready_a:
      if 0 < count_a < 5:
         animal = input('Please try again. Enter an animal: ')
      elif count_a > 4:
         print()
         return False
      if animal == '':
         print('The animal cannot be blank.')
         count_a += 1
      elif animal in ANIMALS:
         print('The animal %s has already been used.' % animal)
         count_a += 1
      else:
         ready_a = True

   # ask for a sound
   sound = input('Enter the sound the animal makes: ')
   # ensure valid entry and limit to 5 tries
   while not ready_s:
      if 0 < count_s < 5:
         sound = input('Please try again. Enter a sound: ')
      elif count_s > 4:
         print()
         return False
      if sound == '':
         print('The sound cannot be blank.')
         count_s += 1
      elif sound in SOUNDS:
         print('The sound %s has already been used.' % sound)
         count_s += 1
      else:
         ready_s = True
         
   print()
   verse(animal, sound)
   return True

# Helper function for verse method
# Parameters: a word
def a_an(word):
   'Modifies a sentence with a or an depending on the following word'
   word = word.lower()
   if word[0] in 'aeiou':
       return 'an'
   else:
       return 'a'

# Helper function for printing first/last line in verse
# No parameters
def first_last():
   'Outputs the first and last line of the verse'
   print('Old McDonald had a farm, E-I-E-I-O.')
