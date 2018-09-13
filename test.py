# The part where this assignment is tripping me up is that it works as 
# intended, but the program which scores the code claims that my program will
# evaluate a negative number and print invalid. I'm thinking about adding True/
# False statements to see if that is what it was looking for, otherwise I don't
# know what to do.

# I successfully completed the assignment. I kept toying around with complexity, but 
# in the end was able to settle on a simple solution.

#hours_worked = int(input())
#if hours_worked < 0 or hours_worked > 137:
#	print('INVALID')
#	hours_worked = int(input())

#pay = hours_worked 

#if hours_worked <= 40:

#	pay = hours_worked * 8
#elif hours_worked <= 50:
#	pay = ((hours_worked - 40) * 9) + (40*8)
#elif hours_worked < 168:
#	pay = ((hours_worked - 50) * 10) + (40*8) + (10*9)
#else:
#	print('INVALID')
#print('YOU MADE', pay, 'DOLLARS THIS WEEK')

hours = int(input())
M = 'YOU MADE '
W = ' DOLLARS THIS WEEK'

check = True

if hours >= 0 and hours <= 168:
	check = True
else:
	check = False
	print('INVALID')
	
if check == True and hours >= 0 and hours <= 40:
	pay = hours * 8
	print(M + str(pay) + W)
elif check == True and hours > 40 and hours <= 50:
	pay = ((hours - 40) * 9) + (40*8)
	print(M + str(pay) + W)
elif check == True and hours > 50:
	pay = ((hours - 50) * 10) + (40*8) + (10*9)
	print(M + str(pay) + W)
else:
	pass
