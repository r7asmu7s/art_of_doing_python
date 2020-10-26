import random

print('Welcome to the GUESS MY NUMBER APP.')

name = input('What is your name? : ').title().strip()

print('Well ' + name + ', I am thinking of a number between 1 and 20.')

number = random.randint(1, 20)

times_guessed = 0

# flag = True

while times_guessed < 5:
  guessed_number = int(input('\nTake a guess: '))
  times_guessed += 1
  if guessed_number == number:
    print('\nGood job ' + name + '! You guessed my number in ' + str(times_guessed) + ' guesses!')
    break
  elif guessed_number < number:
    print('Your guess is too low.')
  else:
    print('Your guess is too high.')

if times_guessed == 5:
  print('\nGAME OVER. The number I was thinking of was ' + str(number) + '.')