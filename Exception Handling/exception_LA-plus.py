# Evan Douglass
# LA11: Exception Handling
# Grade at Plus

# This program averages numbers entered by the user. It is a lesson in
# exception handling.

def main():
   # initialize variables for average calculation
   total = 0
   count = 0
   value = input('Enter a number (\'end\' to exit): ')
   # until the user 'end's the program:
   while(value != 'end'):
      # if value is valid
      if value.isdigit():
         # convert value to int and add to total
         total += int(value)
         # increase count
         count += 1
      # include negative integers
      elif value[1:].isdigit():
         total += int(value)
         count += 1
      # if value not valid
      else:
         # print error
         print('Non-numeric input is skipped.')
      # ask for more values
      value = input('Enter a number (\'end\' to exit): ')

   # output count and average if valid
   print('You entered', count, 'value(s)')
   if count == 0:
      print('The average cannot be calculated.')
   else:
      print('The average value is', total/count)
      
main()
