print('Welcome to the Shipping Accounts Program.')

users = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj']
name = input('\nHello. What is your username? : ').lower().strip()

if name in users:
  print('\nHello, ' + name + '. Welcome back to your account.')
  print('Current shipping prices are are follows: ')

  print('Shipping orders 0 to 100: \t', end='')
  print('$5.10 each')
  print('Shipping orders 100 to 500: \t', end='')
  print('$5.00 each')
  print('Shipping orders 500 to 1000: \t', end='')
  print('$4.95 each')
  print('Shipping orders over 1000: \t', end='')
  print('$4.80 each')

  ship = int(input('\nHow many items would you like to ship? : '))

  for i in range(ship):
    if ship < 100:
      price = 5.10
    elif ship < 500:
      price = 5.00
    elif ship < 1000:
      price = 4.95
    else:
      price = 4.80

  total = price * ship
  total = round(total, 2)
  print('\nTo ship ' + str(ship) + ' items will cost you $' + str(total) + ' at $' + str(price) + ' per item.')

  confirm = input('\nWould you like to place this order? (y/n) : ').lower()

  if confirm == 'y' or confirm == 'yes':
    print('Okay. Shipping your ' + str(ship) + ' items.')
  else:
    print('Order canceled.')
else:
  print('\nYou do not have an account with us. Goodbye.')