print('Welcome to the DATABASE ADMiN PROGRAM.')

log_on = {
  'admin00': 'admin1234',
  'mooman74': 'alskes145',
  'meramo1986': 'kehns010101',
  'nickyD': 'world1star',
  'george2': 'booo3oha',
}

username = input('\nEnter your username: ').strip()

if username in log_on.keys():
  password = input('Enter your password: ')
  # the trickiest part :/
  if password == log_on[username]:
    print('\nHello ' + username + '. You are logged in.')

    if username == 'admin00':
      print('\nHere is the current user database: ')
      for key, value in log_on.items():
        print('Username: ' + key + '\tPassword: ' + value)
    else:
      choice = input('Would you like to change your password? ').lower()
      if choice.startswith('y'):
        new_password = input('Enter your new password: ')
        if len(new_password) < 8:
          print(new_password + ' does not have the minimum eight characters.')
        else:
          log_on[username] = new_password
          print('\n' + username + ', your password is: ' + log_on[username])
      else:
        print('\n' + username + ', your password is: ' + log_on[username])
  else:
    print('Wrong password.')
else:
  print('Username not in database.')