# Evan Douglass
# Textbook Programing Exercise 2: Sales Prediction

# This program predicts a company's profits from user input of
# total sales

# Input total sales
total_sales = float(input('What are the total sales (Do not use commas)? $'))

# Input typical profit as percentage
percent = 0.23

# Calculate predicted profit based on total sales
pred_profit = total_sales * percent

# Display result of above calculation
print('Your predicted profit is: $', format(pred_profit, ',.2f'), sep='')
