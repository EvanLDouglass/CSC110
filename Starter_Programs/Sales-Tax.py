# Evan Douglass
# Ch. 2 Exercises: Sales Tax
#
# This program calculates total sales price of a purchase with two different
# sales taxes.

# input subtotal from user
subtotal = float(input('What is the price of your item(s) (xxxxx.xx): $'))
# input state sales tax
state_tax = 0.05
# input county sales tax
county_tax = 0.025
# calculate total sales tax
tax_total = state_tax + county_tax
# calculate sale total
total = subtotal * (1 + tax_total)
# display subtotal, state tax, county tax, total tax, and total
print('Subtotal: $', format(subtotal, ',.2f'), sep='')
print('State tax:', format(state_tax, '.0%'))
print('County tax:', format(county_tax, '.1%'))
print('Sale total: $', format(total, ',.2f'), sep='')
