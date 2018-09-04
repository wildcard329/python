import random
min = 1
max = 6

roll = "yes"

while roll == "yes" or roll == "y":
	print("Rolling the die...")
	print("The value is...")
	print(random.randint(min,max))
	print(random.randint(min,max))
	roll = input("Roll again? ")
	
