# Evan Douglass
# LA: Jabber
# Grade at check

# This program reads through a file and filters the text for output

# open jabber.txt for reading
jabber = open('jabber.txt')

# open jabber-selected-words.txt for writing
selected_words = open('jabber-selected-words.txt', 'w')

# read whole file and close
text = jabber.readlines()
jabber.close()

# iterate through the alphabet
for letter in 'abcdefghijklmnopqrstuvwxyz':
    
    # write heading to output file for letter
    selected_words.write(letter.upper() + ' words:\n')

    # search file for words with that letter and output to new file
    for line in text:
        line = line.rstrip()
        if letter in line.lower():
            selected_words.write(line + ' ')
    selected_words.write('\n')

# close output file
selected_words.close()

