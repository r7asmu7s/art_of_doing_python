user_0 = {
  'name': 'john',
  'age': '22',
}

user_1 = {
  'name': 'bill',
  'age': '27',
}

user_2 = {
  'name': 'marry',
  'age': '31',
}

users = [user_0, user_1, user_2]

for user in users:
  for key, value in user.items():
    print(key.title() + ':\t' + str(value))
  print('\n')

users = []
for user in range(100):
  new_user = {'name': 'NA', 'age': 0}
  users.append(new_user)

for user in users[:100]:
  print(user)

friends = {
  'bill': ['john', 'tom', 'mary'],
  'tom': ['john', 'bill', 'sue'],
  'mary': ['sue', 'bill', 'tom'],
}

for key, values in friends.items():
  print('\n' + key.title() + "'s friends are: ")
  for value in values:
    print('\t' + value.title())

user_directory = {
  'msmith': {
    'first_name': 'mark',
    'last_name': 'smith',
    'age': 27,
  },
  'ejones': {
    'first_name': 'eddie',
    'last_name': 'jones',
    'age': 42,
  },
}

for user, info in user_directory.items():
  print('\nUsername: ' + user)
  for key, value in info.items():
    print(key + ': ' + str(value))