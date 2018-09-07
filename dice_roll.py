import random
min = 1
max = 6

def getRollAgain():
	rollStr = input("Roll again? ")
	if rollStr.lower() == "yes" or rollStr.lower() == "y":
		return True
	else:
		return False

roll = True
while roll == True:
	print("Rolling the die...")
	print("The value is...")
	print(random.randint(min,max))
	print(random.randint(min,max))
	roll = getRollAgain()
