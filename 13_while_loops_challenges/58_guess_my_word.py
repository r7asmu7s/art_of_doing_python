import random

print('Welcome to the GUESS MY WORD APP.')

game_dict = {"sports": ['basketball', 'baseball', 'soccer', 'football', 'tennis',
'curling'],
"colors": ['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold'],
"fruits": ['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'],
"classes": ['english', 'history', 'science', 'mathematics', 'art', 'health'],
}

game_keys = []

for i in game_dict.keys():
  game_keys.append(i)

# or we can use list comprehension
# game_keys = [i for i in game_dict.keys()]

playing = True

while playing:
  # choosing game category randomly
  game_category = random.choice(game_keys)
  # or
  # game_category = game_keys[random.randint(0, len(game_keys) - 1)]

  # choosing a random game word according to the random game category
  game_word = random.choice(list(game_dict[game_category]))
  # or:
  # game_word = game_dict[game_category][random.randint(0, len(game_dict) - 1)]

  # creating a list based on the string of game word
  game_word_list = list(game_word)
  # creating a blank word, which it's components are dashes, unless changed because of an incorrect guess for the game word
  blank_word = ['-' for i in game_word]

  print('\nGuess a ' + str(len(game_word)) + ' letter word from the following category: ' + game_category)

  # using list comprehension, printing the basic blank word
  print(''.join([str(i) for i in blank_word]))

  guess_count = 0
  
  # a flag allowing to guess
  is_allowed_to_guess = True

  # number of the allowed guesses based on the number of the letters of the game word
  allowed_guesses = len(game_word)

  # while loop for guessing
  while guess_count < allowed_guesses and is_allowed_to_guess:
    guess = input('\nEnter you guess: ').lower().strip()
    # correct guess
    if guess == game_word:
      guess_count += 1
      print('\nCorrect. You guessed the word in ' + str(guess_count) + ' guesses.')
      is_allowed_to_guess = False
      break

    # incorrect guess
    else:
      guess_count += 1
      print('That is not correct. Let us reveal a letter to help you.')
      # a flag to check if the a dash to fill is available in the blank word
      dash_flag = True

      # while loop to fill the dashes in the blank word because of a wrong guess
      while dash_flag:
        # choosing a random dash to fill with a letter
        index = random.randint(0, len(blank_word) - 1)
        if blank_word[index] == '-':
          # filling the dash with the corresponding letter from the correct game word from it's list of letters
          blank_word[index] = game_word_list[index]
          print(''.join([str(i) for i in blank_word]))
          dash_flag = False

  # losing the game 
  else:
    print('\nYou did not guess the word correctly with your ' + str(guess_count) + ' guesses. The word was: ' + game_word)
  
  # play again?
  choice = input('\nWould you like to play again? (YES/NO): ').lower().strip()
  if not choice.startswith('y'):
    playing = False