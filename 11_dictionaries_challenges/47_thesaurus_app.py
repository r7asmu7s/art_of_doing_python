import random

print('Welcome to the Thesaurus App!')
print('\nChoose a word from the thesaurus and I will give you a synonym.')

thesaurus = {
  'hot': ['balmy', 'summary', 'tropical', 'boiling', 'scorching'],
  'cold': ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
  'happy': ['content', 'cheery', 'merry', 'jovial', 'jocular'],
  'sad': ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

print('\nThese are the words in the thesaurus:')

for key in thesaurus.keys():
  print('\t- ' + key)

word = input('\nWhat word would you like to get a synonym for? : ').lower().strip()

# puzzling part :|
if word in thesaurus.keys():
  index = random.randint(0, 4)
  print('A synonym for ' + word + ' is ' + thesaurus[word][index] + '.')
else:
  print('That word is not currently in the thesaurus.')

choice = input('\nWould you like to see the whole thesaurus? (yes/no) : ').lower().strip()

if choice == 'yes' or choice.startswith('y'):
  for key, values in thesaurus.items():
    print('\n' + key.title() + ' synonyms are:')
    for value in values:
      print('\t- ' + value)
else:
  print('\nI hope you enjoyed the program. Thank you.')