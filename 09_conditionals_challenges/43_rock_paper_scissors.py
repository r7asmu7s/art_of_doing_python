import random

print('Welcome to the game of ROCK, PAPER, SCiSSORS.')

rounds = int(input('\nHow many rounds would you like to play? : '))

moves = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

for i in range(1, rounds + 1):
  print('\nRound: ' + str(i))
  print('Player: ' + str(player_score) + '\tComputer: ' + str(computer_score))
  player_choice = input('Time to pick: rock, paper, or scissors? : ').lower().strip()
  computer_choice = random.choice(moves)

  if player_choice in moves:
    print('\tComputer: ' + computer_choice)
    print('\tPlayer: ' + player_choice)

    '''
    scissors cut paper, paper covers rock, rock crushes scissors.
    '''
    if player_choice == 'scissors' and computer_choice == 'paper':
      player_score += 1
      print('\tScissors cut paper!')
      print('You win round ' + str(i) + '.')
    elif player_choice == 'paper' and computer_choice == 'scissors':
      computer_score += 1
      print('\tScissors cut paper!')
      print('\tComputer wins round ' + str(i) + '.')
    elif player_choice == 'paper' and computer_choice == 'rock':
      player_score += 1
      print('\tPaper covers rock!')
      print('You win round ' + str(i) + '.')
    elif player_choice == 'rock' and computer_choice == 'paper':
      computer_score += 1
      print('\tPaper covers rock!')
      print('\tComputer wins round ' + str(i) + '.')
    elif player_choice == 'rock' and computer_choice == 'scissors':
      player_score += 1
      print('\tRock crushes scissors!')
      print('\tYou win round ' + str(i))
    elif player_choice == 'scissors' and computer_choice == 'rock':
      computer_score += 1
      print('\tRock crushes scissors!')
      print('\tComputer wins round ' + str(i))
    else:
      print('\tIt is a tie. How boring!')
      print('\tThis round was a tie.')

  else:
    computer_score += 1
    print('That is not a valid game option!\nComputer gets the point.')

print('\nFinal game results:')
print('\tRounds played: ' + str(rounds))
print('\tPlayer score: ' + str(player_score))
print('\tComputer score: ' + str(computer_score))

if computer_score < player_score:
  print('You WON!')
elif computer_score > player_score:
  print('The machines have WON!') 
else:
  print('THiS WAS A REALLY BOOORiNG GAME!')