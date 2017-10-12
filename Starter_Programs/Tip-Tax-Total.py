# Evan Douglass
# Ch 2 Exercises: Tip, Tax, and Total

# This program calculates a bill including tip and tax

# input charge for food
charge = float(input('Cost of food: $'))

# input sales tax
tax = 0.07

# calculate subtotal (from charge and tax)
subtotal = charge * (1 + tax)

# calculate tip amount
tip = 0.18 * subtotal

# calculate total with tip
total = subtotal + tip

# display each variable/result
print('Charge: $' + format(charge, ',.2f'))
print('Sales tax:', format(tax, '.0%'))
print('Subtotal: $' + format(subtotal, ',.2f'))
print('Tip: $' + format(tip, ',.2f'))
print('Total: $' + format(total, ',.2f'))
