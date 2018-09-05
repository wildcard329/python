#Failed attempt at creating metric <=> standard conversion calculator. 
#Conversions would get error when I called on a variable before it was created
#but when I created the variable and set its value to 0, it retained its 
#initial value regardless of user input. 
#Declare variables
i = 0 
f = 0 
y = 0 
mi = 0
mm = 0
cm = 0
m = 0
km = 0


#Standard to Metric conversions

inch_to_centimeter = i * 2.54

foot_to_centimeter = f * 30.48

yard_to_centimeter = y * 91.44

yard_to_meter = y * 0.914

mile_to_meter = mi * 1609.3

mile_to_kilometer = mi * 1.609

#Metric to Standard conversions

millimeter_to_inch = mm * 0.039

centimeter_to_inch = cm * 0.393

meter_to_inch = m * 39.37

meter_to_foot = m * 3.281

meter_to_yard = m * 1.094

kilometer_to_yard = km * 1093.6

kilometer_to_mile = km * 0.621

#User Input

print('What would you like to convert, "metric to standard", or "standard to metric"?')

while True:
	u_input = input()
	if u_input == 'standard to metric':
		u_input = input('What would you like to convert, \n "inches to centimeters, \n "feet to centimeters", \n "yards to centimeters", \n "yards to meters", \n "miles to meters", \n or "miles to kilometers"?')
		if u_input == 'inches to centimeters':
			i = float(input('How many inches to centimeters?'))
			print(inch_to_centimeter)
		if u_input == 'feet to centimeters':
			f = input('How many feet to centimeters?')
			print(foot_to_centimeter)
		if u_input == 'yards to centimeters':
			y = input('How many yards to centimeters?')
			print(yard_to_centimeter)
		if u_input == 'yards to meters':
			y = input('How many yards to meters?')
			print(yard_to_meter)
		if u_input == 'miles to meters':
			mi = input('How many miles to meters?')
			print(mile_to_meter)
		if u_input == 'miles to kilometers':
			mi = input('How many miles to kilometers?')
			print(mile_to_kilometer) 	 
  
