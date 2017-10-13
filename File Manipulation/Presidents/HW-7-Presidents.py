# Evan Douglass
# HW 7: Presidents
# Grade at challenge

# This program takes records containing information about US presidents,
# sorts it, and outputs the info to a new text file in sentence form.

# main function
def main():
    # read records from presidents file
    in_file = open('presidents.txt', 'r')
    record_list = in_file.readlines()
    in_file.close()
    
    # write info to new file. Order: first name
    out_file_first = open('same_order.txt', 'w')
    outputLines(record_list, out_file_first)

    # write info to new file. Order: last name
    out_file_last = open('last_name.txt', 'w')
    record_list.sort()
    outputLines(record_list, out_file_last)

    # write info to new file. Order: inauguration date
    out_file_date = open('inauguration.txt', 'w')
    
    # sort by inauguration date
    # actually sorts by date left office, then month left office
    sorted_list = sorted(record_list, key=lambda x: (x[-6:], x[-10:]))
    outputLines(sorted_list, out_file_date)

# outputLine function
# Parameters: A line of text, output file name
# Takes a record and writes the information to a text file as a scentence
def outputLines(in_list, out_file):

    # split each record into a list and output information as a sentence
    for record in in_list:
        record = record.strip()
        fields = record.split('\t')
        out_file.write(fields[1] + ' ' + fields[0] + ' was president from '\
               + fields[2] + ' to ' + fields[3] + '.\n')

    out_file.close()

# run program
main()
