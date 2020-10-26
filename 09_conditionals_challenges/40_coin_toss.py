import random

print('Welcome to the Coin Toss App.')

print('\nI will flip a coin a set number of times.')
flips = int(input('How many times would you like me to flip a coin? : '))

question = input('Would you like to see the result of each flip? (y/n) : ').lower().strip()

print('\nFlipping in progress...\n')

flip_results = []
for i in range(flips):
  result = random.randint(1, 2)
  if result == 1:
    flip_result = 'Heads'
  else:
    flip_result = 'Tails'
  flip_results.append(flip_result)
    
  heads = flip_results.count('Heads')
  tails = flip_results.count('Tails')

  if question.startswith('y'):
    print(flip_result)
  if heads == tails:
    print('At ' + str(i + 1) + ' flips, the number of heads and tails were equal at ' + str(heads) + '.')

heads_percentage = heads / flips * 100
heads_percentage = round(heads_percentage, 1)
tails_percentage = tails / flips *100
tails_percentage = round(tails_percentage, 1)

print('\nResults of flipping a coin ' + str(flips) + ' times: ')
print('Sides\t\tCount\t\tPercentage')
print('Heads\t\t' + str(heads) + '/' + str(flips) + '\t\t' + str(heads_percentage) + '%')
print('Tails\t\t' + str(tails) + '/' + str(flips) + '\t\t' + str(tails_percentage) + '%')