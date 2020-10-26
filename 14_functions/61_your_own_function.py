def hello_world(name, age):
  '''
  Greet a user and repeat their age.
  '''
  print('Hello ' + name.title() + '!')
  print('You are ' + str(age) + ' years old.')

def goodbye_world(name = 'nobody', day = 'today'):
  '''
  Say goodbye to a person and wish them a good day.
  '''
  print('Goodbye ' + name.title() + '...')
  print('May you have a good ' + day.title() + '.')

def calc_age(age = 0, interval = 10):
  '''
  Calculate a person's age in x years.
  '''
  print('You are currently ' + str(age) + ' years old.')
  age += interval
  print('In ' + str(interval) + ' years you will be ' + str(age) + '.')

print()
input()
hello_world('bob', 22)

user_name = 'mike'
user_age = 33
hello_world(user_name, user_age)

goodbye_world()
goodbye_world('mike')

calc_age()
calc_age(33)
calc_age(33, 22)
