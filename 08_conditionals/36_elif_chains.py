age = int(input('What is your age? : '))
if age < 18:
  print('You are only ' + str(age) + '!')
  print('You cannot gamble neither drink!')
elif age < 21:
  print('Okay, so you are ' + str(age) + '!')
  print('You can play Blackjack, but you cannot have a drink.')
elif age < 100:
  print('Okay, good. You are ' + str(age) + '!')
  print('You can play Blackjack and have a drink.')
else:
  print('What are you doing out at a casino?!')

num = int(input('\nPut a number in: '))
if num < 5:
  print('That is a small number.')
elif num < 10:
  print('That is sort of small.')
elif num < 15:
  print('That is a medium number.')
elif num < 20:
  print('That is sort of medium.')
elif num < 25:
  print('That is a large number.')
elif num == 40:
  print('I love that number!')
else:
  print('That number is HUGE!')