layers = int(input('Enter number of layers in cube structure. '))
sides = 0
for i in range(0,layers+1):
    sides += i**2
    
total = (layers + 1)**3 + layers**3 + 6*sides
time = 15 * total / 60
print('Total number of cubes: ',total)
print('It should take ',time,' hours to fold all those cubes.')
