import random

rNumber = random.randrange(100) + 1

guess = ''

guesses = []

counter = 1

while guess != rNumber and counter < 10:
  guess = int(input('Guess the random number between 1 and 100. '))
  if guess != rNumber:
    guesses += str(int(guess))
    counter += 1
    print('Previous attempts: ', guesses)
  if guess < rNumber:
    print('Higher')
  elif guess > rNumber:
    print('Lower')
    
if guess == rNumber:
  print('Congradulations! That was the number! Attempts: ',counter)
