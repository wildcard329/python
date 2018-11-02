import random

player = input('What is your name? ')

print('Welcome',player,'''\b! Today instead of you guessing my number, 
I will guess yours. I have ten turns to guess your number,
I win if I guess it and you win if I can\'t guess your number
in ten turns. Please be honest in your feedback.

Please select a number between 1 and 100, but don't tell me what it is, I will guess it.''')

min = 1
max = 100
counter = 1

guess = random.randint(min, max)
print('I am guessing the number is ', guess)

feedback = input('[h]igher, [l]ower, or [c]orrect? ')
while feedback != 'c' and counter < 10:
  if feedback == 'h':
    min = guess + 1
  elif feedback == 'l':
    max = guess - 1
  counter += 1
  guess = random.randint(min, max)
  print(guess)
  feedback = input('[h]igher, [l]ower, or [c]orrect? ')
  
if feedback == 'c':
  print('Yay!!! I won!!! Good Game,',player,'\b!')
  
if counter == 10:
  print('Oh, darn. I ran out of guesses. You win,',player,'\b!')
