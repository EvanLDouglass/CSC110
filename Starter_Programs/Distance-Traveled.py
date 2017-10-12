# Evan Douglass
# Ch. 2 Exercises: 5. Distance Traveled
#
# This program is intended to calculate and display the distance a car will
# travel in 6, 10 and 15 hours at 70 mph, assuming a straight path and no
# obsticles.

# input speed of car in mph
speed = 70

# input time periods (in hours)
time_1 = 6
time_2 = 10
time_3 = 15

# calculate distance traveled for each time period
distance1 = speed * time_1
distance2 = speed * time_2
distance3 = speed * time_3

# display the distance traveled for each time period
print('A car traveling 70 mph will go', distance1, 'miles in 6 hrs,', distance2, \
      'miles in 10 hrs, and', distance3, 'miles in 15 hrs.')
