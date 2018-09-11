

while True:
	convert = input('Convert to decimal or binary? ')
	if convert == 'decimal':
		convert = int(input('Please enter a binary value '),2)
		print(convert)
	elif convert == 'binary':
		convert = bin(int(input('Please enter a number ')))
		print(convert)
	elif convert == 'q':
		break
	else:
		print('Please enter a valid option. ')
