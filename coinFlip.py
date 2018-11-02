import random

heads = 0
tails = 0

for i in range(1,101):
  flip = random.randrange(2)
  if flip == 0:
    tails += 1
  elif flip == 1:
    heads += 1
    
print('Heads: ', heads, 'Tails: ', tails)
