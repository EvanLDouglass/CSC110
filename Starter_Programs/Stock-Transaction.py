# Evan Douglass
# Ch. 2 Exercises: Stock Transaction

# This program calculates the details of an example stock transaction

# Purchasing of Stock
# input # of shares purchased
shares_bought = 2000
# input price per share
price_bought = 40.00 # $/share
# input commission amount (%)
comm_perc = 0.03
# calculate price paid before commission
purchase = shares_bought * price_bought
# calculate commission amount ($)
comm_bought = purchase * comm_perc
# calculate price after commission
tot_purch = purchase - comm_bought

# Selling of Stock
# input # of shares sold
shares_sold = 2000
# input price per share
price_sold = 42.75 # $/share
# calculate total sales
sale = shares_sold * price_sold
# calculate commission amount ($)
comm_sale = sale * comm_perc
# calculate sales after commission
tot_sale = sale - comm_sale
# calculate total revenue for Joe
revenue = tot_sale - tot_purch

# display amount paid for stock
print('Amount paid for stock: $' + format(purchase, ',.2f'))
# display commission for purchase
print('Commission for purchase: $' + format(comm_bought, ',.2f'))
# display amount for which stock sold
print('Amount for which stock sold: $' + format(sale, ',.2f'))
# display commission for sale
print('Commission for sale: $' + format(comm_sale, ',.2f'))
# display total revenue
print('Joe\'s Revenue: $' + format(revenue, ',.2f'))
