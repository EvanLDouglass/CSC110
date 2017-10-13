import oldMcDonald

# driver function
def main():

   # print the title
   oldMcDonald.title()

   # print the first three verses
   oldMcDonald.verse('chicken', 'cluck')
   oldMcDonald.verse('cow', 'moo')
   oldMcDonald.verse('duck', 'quack')

   # ask for more verses
   while oldMcDonald.query_verse():
      pass

   # say goodnight, gracie
   print('Thanks for singing with me.')

# run the program
main()
