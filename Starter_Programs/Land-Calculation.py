# Evan Douglass
# Ch.2 Exercsize 3: Land Calculation
#
# This program is intended to calculate the number of acres on a tract of land
# from the total square footage.

# input square footage from user
sq_ft = float(input('What is the total square footage of land?: '))
# input acre to square foot equivalency
one_acre = 43560.0 #ft
# Convert square feet into acres
total = sq_ft / one_acre
# Display results
print('The tract of land is', format(total, ',.2f'), 'acres')
