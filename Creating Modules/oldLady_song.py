import oldLady

# the driver function
def main():

   # print out the title
   oldLady.title()

   # print out the verses
   for num in range(len(oldLady.ANIMALS)):
      oldLady.verse(num)

# run the program
main()
