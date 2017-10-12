# Evan Douglass
# Time Calculator

# This program converts seconds into days, hours and minutes

# Main function: time calculator
def main():
    # Get seconds
    seconds = int(input('Enter time interval in seconds (integers only): '))

    # If seconds less than 60
    if seconds < 60:
        #Output seconds
        print(seconds, 'seconds')
        print()

    # If seconds between 60 and 3600
    elif 60 < seconds < 3600:
        # Calculate minutes, seconds
        minutes = seconds // 60
        seconds = int(seconds % 60)
        # Output minutes and seconds
        print(minutes, 'minutes and', seconds, 'seconds')
        print()

    # If seconds between 3600 and 86,400
    elif 3600 < seconds < 86400:
        # Calculate hours, minutes, seconds
        hours = seconds // 3600
        minutes = int((seconds / 60) % 60)
        seconds = int(seconds % 60)
        # Output hours, minutes, seconds
        print(hours, 'hours,', minutes, 'minutes and', seconds, 'seconds')
        print()

    # If seconds greater than 86,400
    elif seconds > 86400:
        # Calculate days, hours, minutes, seconds
        days = seconds // 86400
        hours = int((seconds / 3600) % 24)
        minutes = int((seconds / 60) % 60)
        seconds = int(seconds % 60)
        # Output days, hours, minutes, seconds
        print(days, 'days,', hours, 'hours,', minutes, 'minutes and', seconds,
              'seconds')
        print()

# Again? function
# Asks user if they want to go again
def again():
    go_again = input('Would you like to try another time? Enter Y/N\n')
    go_again = go_again.upper()
    if go_again == 'Y':
        print()
        main()
        again()
    elif go_again == 'N':
        raise SystemExit
    else:
        print('I did not understand that.')
        print()
        again()

# Call main
main()
again()
