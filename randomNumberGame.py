import random

rNumber = random.randrange(10) + 1

guess = ''

guesses = []

while guess != rNumber:
  guess = int(input("Guess the random number between 1 and 10. '))
  if guess != rNumber:
  guesses += str(guess)
  print('Previous attempts: ', guesses)
  
if guess == rNumber:
  print('Congradulations! That was the random number!')
