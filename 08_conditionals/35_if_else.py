colors = ['green', 'red', 'blue']

for color in colors:
  print(color)

for color in colors:
  if color == 'red':
    print(color.upper())
    print('I LOVE the color ' + color.upper())
  else:
    print(color)
    print('The color ' + color + ' is okay...')

age = int(input('\nWhat is your age? : '))
if age >= 21:
  print('Have a drink!')
else:
  print('Ah, no drinks for your!')

first_name = 'Bill'
last_name = 'Smith'
if first_name == 'Dave' and last_name == 'Smith':
  print('You are a cool guy!')
else:
  print('Not cool enough!')

if first_name == 'John' or last_name == 'Jones':
  print('You are a great guy!')
else:
  print('Not great enough!')