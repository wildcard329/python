

while True:
	x = input('Please enter a number, or enter q to quit. ')
	if x == 'q':
		break
	else:
		x = int(x)
	y = input('Please enter a number, or enter q to quit. ')
	if y == 'q':
		break
	else:
		y = int(y)
	print('Please enter the operator you would like to use for these numbers. a for add, s for subtract, m for multiply, d for divide. Enter q to quit.')
	op = input()
	if op == 'a':
		print(x + y)
	elif op == 's':
		print(x - y)
	elif op == 'm':
		print(x * y)
	elif op == 'd':
		print(x / y)
	elif op == 'q':
		break
	else:
		print('Please enter a valid option.')
