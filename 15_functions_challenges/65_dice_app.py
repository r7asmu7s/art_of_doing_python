import random

def dice_sides():
  '''
  ask the user how many sides on their die
  '''
  sides = int(input('\nHow many sides would you like on your dice? : '))
  return sides

def dice_number():
  '''
  ask the user how many dice to tole
  '''
  number = int(input('\nHow many dice would you like to roll? : '))
  return number

def roll_dice(sides, number):
  '''
  simulate rolling the dice
  '''
  dice = []
  print('\nYou rolled ' + str(number) + ' ' + str(sides) + ' sided dice.')
  print('\n- - - - Results are as followed: - - - -')
  for i in range(number):
    value = random.randint(1, sides)
    print('\t' + str(value))
    dice.append(value)
  return dice

def sum_dice(dice):
  '''
  add all values of dice in a list
  '''
  # using built-in sum function
  # print('The total value of your roll is: ' + str(sum(dice)) + '.')
  # using our own method
  total = 0
  for die in dice:
    total += die
  print('The total value of your roll is: ' + str(total) + '.')

def roll_again():
  '''
  ask the user to roll again
  '''
  choice = input('\nWould you like to roll again? (y/n) : ').lower()
  if choice != 'y':
    roll = False
  else:
    roll = True
  return roll

# the main code
print('Welcome to the Python Dice App.')
rolling = True
while rolling:
  # get info for the type of dice
  d_sides = dice_sides()
  d_number = dice_number()

  # roll the dice
  my_dice = roll_dice(d_sides, d_number)
  sum_dice(my_dice)

  # roll again?
  rolling = roll_again()

print('Thank you for using the Python Dice App.')