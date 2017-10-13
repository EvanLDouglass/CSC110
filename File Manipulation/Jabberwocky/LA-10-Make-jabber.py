# Evan Douglass
# LA10: Making jabber.txt
# Grade at Plus

# This program takes poems/text from a file and outputs a new file with
# each word on a new line. It can also be run from the command line.

import sys

# main function
# represents program structure
def main():
    try:
        # if only script file given, or opened in IDLE:
        if len(sys.argv) == 1:
            # set up files
            in_file = open('jabberwocky.txt', 'r')
            out_file = open('jabber-out.txt', 'w')
            # run program
            processing(in_file, out_file)
            message('jabber-out.txt')
            
        # if 2 args given:
        elif len(sys.argv) == 3:
            # try opening both as read files
            try:
                # iterate backwards to check 2nd arg first
                for file in sys.argv[2:0:-1]:
                    in_file = open(file, 'r')
                    # create output file
                    file2 = file.rstrip('.txt') + '-out.txt'
                    out_file = open(file2, 'w')
                    # run program
                    processing(in_file, out_file)
                    message(file2)
                    
            # if second arg not found, use as output file
            except FileNotFoundError:
                in_file = open(sys.argv[1], 'r')
                out_file = open(sys.argv[2], 'w')
                # run program
                processing(in_file, out_file)
                message(sys.argv[2])
                
        # if one or three+ args use all as read files 
        else:
            for file in sys.argv[1:]:
                try:
                    in_file = open(file, 'r')
                    # create output file
                    file2 = file.rstrip('.txt') + '-out.txt'
                    out_file = open(file2, 'w')
                    # run program
                    processing(in_file, out_file)
                    message(file2)
                except FileNotFoundError:
                    print('File', file, 'not found.')
                    
    # print error if an arg is not found
    except FileNotFoundError:
        print('File not found.')
            
# processing function
# parameters: the input and output files
# reads a text file and outputs each word to it's own line
# it skips the first three lines of the input file
def processing(in_file, out_file):
    # pass over first three lines
    in_file.readline()
    in_file.readline()
    in_file.readline()
    line = in_file.readline()
    # while line is not an empty string:
    while line:
        # if line is not only '\n':
        if line != '\n':
            # seperate each word
            line = line.strip().split()
            # write each word on a new line to out-file
            for word in line:
                out_file.write(word + '\n')
            # read the next line from in-file
            line = in_file.readline()
        else:
            line = in_file.readline()
    # close files
    in_file.close()
    out_file.close()
    
# success message function
# parameter: output file name
# prints a success message upon completion of the program
def message(file):
    print('The words were written to', file + '.')

# run the program
main()
