# Evan Douglass
# HW 8: Children's song, the reprise
# Grade at challenge

'''This module defines several variables and methods used to print the
children's song "There was an Old Lady"'''

# Animals used in the song
ANIMALS = ('fly.', 'spider,', 'bird.', 'cat.',
   'dog.', 'goat.', 'cow.', 'horse.')

# A list of the second line in each verse, and the final line in the song
LINES = ('I don\'t know why she swallowed the fly.',
   'That wriggled and jiggled and tickled inside her.',
   'How absurd to swallow a bird.',
   'Imagine that to swallow a cat.',
   'My, what a hog, to swallow a dog.',
   'She just opened her throat and in walked the goat.',
   'I don\'t know how she swallowed a cow.',
   'She\'s dead, of course.',
   )

# Title method
# No Parameters
def title():
   'The title function prints the title to the song'
   print('There was an Old Lady')
   print()

# Verse method
# Parameter: the index of the verse
def verse(n):
   'The verse function prints each verse to the song, seperated by blank lines.'
   print('There was an old lady who swallowed a %s' % ANIMALS[n])
   print(LINES[n])
   if n == 0:
      print('Perhaps she\'ll die.')
      print()
   elif 0 < n < len(ANIMALS)-1:
      for animal in ANIMALS[n:0:-1]:
         print('She swallowed the', animal[0:-1], 'to catch the',
               ANIMALS[ANIMALS.index(animal)-1])
         if ANIMALS[ANIMALS.index(animal)-1] in ANIMALS[0:2]:
            print(LINES[ANIMALS.index(animal)-1])
      print('Perhaps she\'ll die.')
      print()
   else:
      print()
