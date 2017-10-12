# Evan Douglass
# Ch. 2 Exercises: Male and Female Percentages

# This program calculates the percentage of males and females in a given class.

# input number of males
num_males = int(input('How many males are in the class? '))

# input number of females
num_females = int(input('How many females are in the class? '))

# calculate total class size
class_size = num_males + num_females

# calculate percent of males
perc_male = num_males / class_size

# calculate percent of females
perc_female = num_females / class_size

# display the percentage of males and females
print('The class is', format(perc_male, '.0%'), 'male, and', \
      format(perc_female, '.0%'), 'female.')
