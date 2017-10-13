# Evan Douglass
# LA: Laughter
# Grade at plus

# This program is a learning activity involving input validation. It asks for a name
# and evilness values then checks to make sure they are valid. If they are, it
# outputs a greeting and laugh appropriate to the evilness level.

def main():
    # initialize count variable
    count = 0
    # for 3 trys:
    while count < 3:
        # get name
        name = input('Enter the name: ')
        # if name is empty:
        if name.strip() == '':
            # print error and restart loop
            print('Error in input. Name cannot be blank.')
            count += 1
        # if name is valid, move on
        else:
            break
    # if count has been exceeded, set name to Magneto by default
    if count == 3:
        print()
        print('Exceeded maximum trys. Name set to "Magneto".')
        name = 'Magneto'
        print()
        
    # get rating and check validity
    # while the program needs a rating:
    needs_rating = True
    while needs_rating:
        # get rating
        rating = input('Enter the evilness rating: ')
        # try converting rating to int type
        try:
            rating = int(rating)
        # if exception raised, print error
        except ValueError:
            print('Error in input. Rating must be an integer value.')
            continue
        if -7 <= rating < 0:
            # change laugh to Ho repeated by the absolute value of the rating
            laugh = 'Ho' * abs(rating)
            # end loop
            needs_rating = False
        # if rating is 0:
        elif rating == 0:
            # change laugh to Hee Hee
            laugh = 'Hee Hee'
            # end loop
            needs_rating = False
        # if rating is over 10
        elif 1<= rating <= 7:
            # change laugh
            laugh = 'Bwa' + 'ha' * rating
            # end loop
            needs_rating = False
        else:
            print('Error in input. Choose a number between -7 and 7, inclusive.')
            
    # output a message
    print('My name is %s. %s.' % (name, laugh))

# run program
main()
