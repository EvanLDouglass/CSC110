# Evan Douglass
# HW 6: Shopping List
# Grade at challenge

# This program creates a shopping list that the user can add to, review, and
# remove items from. It stores the list in a file when user is done.

# create a shared list
theList = []
# read/write file
THE_LIST = 'shopping-list.txt'

# print menu function
# no parameters
# prints the program menu for the user
def printMenu():
    # print several lines with the commands for the program
    print('Here are the list of commands:')
    print('  -p   : Print the list')
    print('  -e   : Empty the list')
    print('  -r n : Remove item n from the list')
    print('  -x   : Exit')
    print('  -h   : Print this list of commands')

# add item to list function
# parameter: an item the user wants to add to the list
# adds user input to the grocery list
def addToList(item):
    # if item is empty, print error
    if item.strip() == '':
        print('Shopping list items cannot be blank.')
    # if item is a duplicate print error
    elif item in theList:
        print(item, 'is already in the list.')
    # append item to list
    else:
        theList.append(item)
    # report the addition and the number of items in the list
        print(item, 'added to the list.')

# get input function
# no parameters
# outputs the number of items in the list
def getInput():
    # report the number of items in the list
    print('You have', len(theList), 'items on your list.')
    # ask for command
    return input('Enter an item or command: ')

# print list function
# no parameters
# outputs the numbered items in the list
def printList():
    print('Your shopping list:')
    # for each item in the list:
    for item in theList:
        # print the item with it's index + 1
        print('  ', str(theList.index(item) + 1) + '.', item)

# empty list function
# no parameters
# empties the entire list
def emptyList():
    # empty each item in the list
    while theList != []:
        for item in theList:
            theList.remove(item)
    # print confirmation message
    print('The list was emptied.')

# remove from list function
# parameter: an item the user wants removed or the index of the item
# removes a specified item from the list
def removeFromList(item):
    # try to remove item
    try:
        theList.remove(item)
        print(item, 'removed from the list.')
    except ValueError:
        # try converting to an integer
        try:
            item = abs(int(item))
            del theList[item - 1]
            print('item number', item, 'removed from the list.')
        # if exception raised, print error
        except ValueError:
            print('Item not located.')
        except IndexError:
            print('Item not located.')

# start program function
# no parameters
# outputs a welcome message
def startProgram():
    print('Welcome to the XYZ Shopping List Program')
    try:
        oldList = open(THE_LIST, 'r')
        line = oldList.readline()
        while line:
            theList.append(line.rstrip('\n'))
            line = oldList.readline()
        oldList.close()
    except FileNotFoundError:
        pass
    

# end program function
# no parameters
# outputs a goodby message
def endProgram():
    newList = open(THE_LIST, 'w')
    for item in theList:
        newList.write(item + '\n')
    newList.close()
    if theList != []:
        print('Your list was saved to shopping-list.txt')
    print('Thank you for using the XYZ Shoppling List Program.')    

# main function
# no parameters
# controls program flow
def main():
    # welcome message, menu, and prompt
    startProgram()
    printMenu()
    item = getInput()
    # while continue is True
    cont = True
    while cont:
        # if user enters unrecognized command:
        # first check prevents an index error from an empty item
        if len(item) > 1 \
           and item[0] == '-' \
           and item[1] not in ['p', 'e', 'r', 'x', 'h']:
            # output error message
            print('Unrecognized command.')
        # prevents addition of lone "-" to list
        elif item.strip() == '-':
            print('Unrecognized command.')
        # if commands recognized, execute the commands
        elif item.strip() == '-x':
            # exit loop
            break
        elif item.strip() == '-e':
            emptyList()
        elif item.strip() == '-p':
            printList()
        elif item.strip() == '-h':
            printMenu()
        elif item[:2] == '-r':
            # strip command from item
            n = item.lstrip('-r ')
            # remove item from list
            removeFromList(n)
        # if user enters an item:
        else:
            # add item to the list
            addToList(item)
        # prompt user for item or command
        item = getInput()
    # exit program
    endProgram()

# run program
main()
