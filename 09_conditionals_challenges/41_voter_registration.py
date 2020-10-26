print('Welcome to the VOTER REGiSTRATiON APP.')

# getting user input
name = input('What is you name? : ').title()
age = int(input('How old are you? : '))

parties = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']

flag = True

while flag:
  if age >= 18:
    print('\nCongratulations ' + name + '! You are old enough to register to vote.')
    print('\nHere is a list of political parties to join:')

    # printing the list of parties.
    for party in parties:
      print('\t-' + party)

    # asking the user to choose a party.
    join = input('\nWhat party would you like to join? : ').title()

    # printing the result.
    if join in parties:
      print('\nCongratulations ' + name + '! You have joined the ' + join + ' party!')
      if join == 'Republican' or join == 'Democratic':
        print('It is a major party!')
      elif join == 'Independent':
        print('You are and independent person!')
      else:
        print('That is not a major party.')
      flag = False

    else:
      print('\nThat is no a given party.')

  else:
    print('You are not old enough to register to vote.')
    flag = False