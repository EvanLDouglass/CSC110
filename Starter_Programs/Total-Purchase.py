# Evan Douglass
# Ch. 2 Exercise 4: Total Purchase

# This program is intended to calculate the total sales price from 5 items

# display directions
print('Input prices for items when prompted. Do not use commas. ' + \
      'Format: xxxxx.xx')
# input items
item_1 = float(input('Price of 1st item: $'))
item_2 = float(input('Price of 2nd item: $'))
item_3 = float(input('Price of 3rd item: $'))
item_4 = float(input('Price of 4th item: $'))
item_5 = float(input('Price of 5th item: $'))

# input sales tax
sales_tax = 0.07

# Calculate subtotal and total
sub_total = item_1 + item_2 + item_3 + item_4 + item_5
total = sub_total * (1 + sales_tax)

# display subtotal, sales tax, total on different lines
print('Subtotal: $' + format(sub_total, '7,.2f'))
print('Sales tax:', format(sales_tax, '.0%'))
print('Total: $' + format(total, '7,.2f'))                                                                   
