# Evan Douglass
# Lab 3: Section Times
# Grade at plus

# This program outputs a meeting time for a user's class based on the
# section number

# Gather information from the user
dept = input('Enter the department code: ')
course = input('Enter the course number: ')
section = input('Enter the section number: ')

# Determine when the class meets
if section == '01':
    meeting_time = '8:00 - 8:50 am, Daily'
elif section == '02':
    meeting_time = '9:00 - 9:50 am, Daily'
elif section == '03':
    meeting_time = '10:00 - 10:50 am, Daily'
elif section == '04':
    meeting_time = '11:00 - 11:50 am, Daily'
elif section == '05':
    meeting_time = '12:00 - 1:05 pm, MTWTh'
elif section == '06':
    meeting_time = '1:15 - 2:20 pm, MTWTh'
elif section == '08':
    meeting_time = '6:00 - 8:20 pm, MW'
elif section == '09':
    meeting_time = '6:00 - 8:20 pm, TTh'
else:
    print('ERROR: Unrecognized section number.')
    # Exit program by calling a "SystemExit" (method found on Stack Overflow)
    raise SystemExit

# Ensure department code is upper case
if dept != dept.upper():
    dept = dept.upper()
    print('WARNING: department code is not upper-case.')
# Course number warning if less than 3 digits
if len(course) != 3:
    print('WARNING: course number is not 3-digits.')
# Course number "not numeric" error condition
if not course.isdigit():
    print('WARNING: course number is not numeric.')
    
# Output the information to the user
print('Your course', dept, course + '-' + section, 'meets', meeting_time)
