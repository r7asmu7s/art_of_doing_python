import random

print('-------------POWER BALL SiMULATOR-------------')

# determine the size of the lottery
# get the number of white balls
white_balls = int(input('\nHow many white balls to draw from for the 5 winning numbers? (Normally 69) : '))

if white_balls < 5:
  white_balls = 5

# get the number of red balls
red_balls = int(input('How many red balls to draw from for the power ball? (Normally 26) : '))

if red_balls < 1:
  red_balls = 1

# calculate the odds of winning this specific lottery
odds = 1


for i in range(5):
  '''
  example multiplication for generating odds to win
  (69 * 68 * 67 * 66 * 65) * 26 / 120 # normal power ball
  (20 * 19 * 18 * 17 * 16) * 4 / 120 # for 20 white balls and 4 red balls
  '''
  odds *= white_balls - i
  print(odds)

odds *= red_balls / 120

print('You have a 1 in ' + str(odds) + ' chance of winning this lottery.')

# get ticket interval
ticket_interval = int(input('Purchase ticket in what interval? : '))

# generate the winning lottery numbers
# generate white balls for the ticket
winning_numbers = []

while len(winning_numbers) < 5:
  number = random.randint(1, white_balls)
  if number not in winning_numbers:
    winning_numbers.append(number)

winning_numbers.sort()

# generate red balls for the ticket
number = random.randint(1, red_balls)
winning_numbers.append(number)

# simulate the powerball drawing
print('\n-------------WELCOME TO THE POWER BALL-------------')
print("\nTonight's winning numbers are: ", end='')
for number in winning_numbers:
  print(str(number), end=' ')

input("\nPress 'Enter' to begin purchasing tickets. ")

# initialize variables to aid in the selling of tickets
ticket_purchased = 0
active = True
tickets_sold = []

# run the lottery if we haven't purchased the winning ticket and we still want to play
while winning_numbers not in tickets_sold and active:
  # make a new lottery ticket for the user to buy
  lottery_numbers = []
  # get the white balls for the ticket
  while len(lottery_numbers) < 5:
    number = random.randint(1, white_balls)
    if number not in lottery_numbers:
      lottery_numbers.append(number)
  
  lottery_numbers.sort()

  # get the red ball for the ticket
  number = random.randint(1, red_balls)
  lottery_numbers.append(number)

  # this current ticket has not yet been sold
  if lottery_numbers not in tickets_sold:
    ticket_purchased += 1
    tickets_sold.append(lottery_numbers)
    print(lottery_numbers)
  # the ticket has already been sold and is a loser don't sell again
  else:
    print('Losing ticket generated; disregard...')

  # check if the user wants to continue buying ticket in the indicated interval
  if ticket_purchased % ticket_interval == 0:
    print(str(ticket_purchased) + ' tickets purchased so far with no winners... ')
    choice = input('\nKeep purchasing tickets? (y/n) : ').lower()
    if not choice.startswith('y'):
      active = False
    
# the lottery is now over
# the winning ticket is purchased and the lottery is won
if lottery_numbers == winning_numbers:
  print('\nWinning ticket numbers: ', end='')
  for number in lottery_numbers:
    print(str(number), end=' ')
  print('\nPurchased a total of ' + str(ticket_purchased) + ' tickets.')
# we didn't purchased the winning ticket and we gave up
else:
  print('\nYou bought ' + str(ticket_purchased) + ' tickets and still lost.')
  print('Better luck next time!')