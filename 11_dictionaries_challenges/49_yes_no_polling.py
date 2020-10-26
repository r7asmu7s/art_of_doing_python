print('Welcome to the YES/NO POLLiNG APP.')

issue = input('\nWhat is the yes/no issue you will be voting on today? : ')
vote_number = int(input('What is the number of voters you will allow on the issue? : '))
password = input('Enter a password for the polling results: ')

yes = 0
no = 0
results = {}

for i in range(vote_number):
  name = input('\nEnter your full name: ').title().strip()
  if name in results.keys():
    print('\nSorry, it seems that someone with that name has already voted.')
  else:
    print('\nHere is our issue: ' + issue )
    choice = input('What do you think? YES/NO: ').lower().strip()
    if choice == 'yes' or choice == 'y':
      choice = 'yes'
      yes += 1
    elif choice == 'no' or choice == 'n':
      choice = 'no'
      no += 1
    else:
      print('That is not a YES/NO answer, but okay...')
    
    # add vote to dictionary results
    # the trickiest part :/
    results[name] = choice
    print('\nThank you ' + name + '. Your vote of ' + results[name] + ' has been recorded.')

# show who actually voted
total_votes = len(results.keys())
print('\nThe following ' + str(total_votes) + ' peaple voted: ')
for key in results.keys():
  print(key)

# summarize the voting results
print('\nOn the following issue: ' + issue)
if yes > no:
  print('YES wins! ' + str(yes) + ' votes to ' + str(no) + '.')
if yes < no:
  print('NO wins! ' + str(no) + ' votes to ' + str(yes) + '.')
else:
  print('It was a tie. ' + str(yes) + ' votes to ' + str(no) + '.')

# admin access
guess = input('\nTo see the voting results, enter the admin password: ')
if guess == password:
  for key, value in results.items():
    print('Voter: ' + key + '\tVote: ' + value)
  else:
    print('Sorry, that is not the correct password.')