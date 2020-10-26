def draw_board(character_list):
  '''
  print a game board; either a number board or a tic tac toe board.
  '''
  print('\n\t    TiC-TAC-TOE')
  print('\t~~~~~~~~~~~~~~~~~~')
  print('\t|| ' + character_list[0] + ' || ' + character_list[1] + ' || ' + character_list[2] + ' ||')
  print('\t~~~~~~~~~~~~~~~~~~')
  print('\t|| ' + character_list[3] + ' || ' + character_list[4] + ' || ' + character_list[5] + ' ||')
  print('\t~~~~~~~~~~~~~~~~~~')
  print('\t|| ' + character_list[6] + ' || ' + character_list[7] + ' || ' + character_list[8] + ' ||')
  print('\t~~~~~~~~~~~~~~~~~~')


def get_player_input(player_character, character_list):
  '''
  get a player's move until it is a valid move on the board with no piece currently there.
  '''
  while True:
    # get user input
    player_move = int(input(player_character + ': Where would you like to place your piece? (1 ~ 9): '))
    # move is on board
    if player_move > 0 and player_move < 10:
      # move is an empty spot
      if character_list[player_move - 1] == '-':
        return player_move
      else:
        print('That spot has already been chosen. Try again.')
    else:
      print('That is not a spot on the board. Try again.')


def place_character_on_board(player_character, player_move, character_list):
  '''
  put a player's character at the correct spot on the board.
  '''
  char_list[player_move - 1] = player_character

def is_winner(player_character, character_list):
  '''
  return a boolean if the given player is a winner.
  '''
  return (
    # checking for rows
    (character_list[0] == player_character and character_list[1] == player_character and character_list[2] == player_character)
    or 
    (character_list[3] == player_character and character_list[4] == player_character and character_list[5] == player_character)
    or
    (character_list[6] == player_character and character_list[7] == player_character and character_list[8] == player_character)
    or
    # checking for columns
    (character_list[0] == player_character and character_list[3] == player_character and character_list[6] == player_character)
    or
    (character_list[1] == player_character and character_list[4] == player_character and character_list[7] == player_character)
    or
    (character_list[2] == player_character and character_list[5] == player_character and character_list[8] == player_character)
    or
    # checking for diagonals
    (character_list[0] == player_character and character_list[4] == player_character and character_list[8] == player_character)
    or
    (character_list[2] == player_character and character_list[4] == player_character and character_list[6] == player_character)
    )


# main code
# define variables
player_1 = 'X'
player_2 = 'O'
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
char_list = ['-'] * 9

# draw the initial state of the game board
draw_board(num_list)
draw_board(char_list)

while True:
  # player 1's turn
  # get the player's move
  move = get_player_input(player_1, char_list)
  # put move on board
  place_character_on_board(player_1, move, char_list)
  # redraw game board
  draw_board(num_list)
  draw_board(char_list)
  # check to see if player 1 won
  if is_winner(player_1, char_list):
    print('Player 1 wins.')
    break
  # check to see if it's a tie
  elif '-' not in char_list:
    print('The game was a tie.')
    break

  # player 2's turn
  # get the player's move
  move = get_player_input(player_2, char_list)
  # put move on board
  place_character_on_board(player_2, move, char_list)
  # redraw game board
  draw_board(num_list)
  draw_board(char_list)
  # check to see if player 1 won
  if is_winner(player_2, char_list):
    print('Player 2 wins.')
    break
