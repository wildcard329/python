# Solution in python to first scenario on project euler. 
# Project called for solution for the sum of the multiples of 3 and 5 below 1000.
# In Python, multiples can be added through use of the % operator.
# In this scenario, modulo 3 and 5 were used to get the sum, but because
# modulo 15 got counted twice as a result of this method, after the script
# runs we add var_3 to var_5 and subtract var_15 (which only counted modulo 15 once).

counter = 0
var_3 = 0
var_5 = 0
var_15 = 0

while counter < 999:
	counter += 1
	if counter % 3 == 0:
		var_3 += counter
	if counter % 5 == 0:
		var_5 += counter
	if counter % 15 == 0:
		var_15 += counter
print(var_3+var_5-var_15)

