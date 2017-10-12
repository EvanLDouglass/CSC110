# Evan Douglass
# Ch. 2 Exercsises: Ingredient Adjuster

# This program adjusts the needed amount of ingredients for a cookie recipe
# based on the number of cookies the user wants to make
# Recipe: 1.5 cups sugar, 1 cup butter, 2.75 cups flour. Makes 48 cookies.

# input desired number of cookies
cookies = int(input('How many cookies do you want to make? '))
# calculate percentage of from 48
percent = cookies / 48
# calculate new amounts of ingredients needed
sugar = 1.5 * percent
butter = 1.5 * percent
flour = 2.75 * percent
# display the new recipe for n cookies
print('Adjusted Cookie Recipe')
print(format(sugar, '.2f'), 'cup(s) of sugar')
print(format(butter, '.2f'), 'cup(s) of butter')
print(format(flour, '.2f'), 'cup(s) of flour')
