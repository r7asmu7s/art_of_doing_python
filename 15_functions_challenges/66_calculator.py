def add(a, b):
  '''
  add two numbers and return the sum
  '''
  summation = round(a + b, 4)
  print('\nThe sum of ' + str(a) + ' and ' + str(b) + ' is ' + str(summation))
  return str(a) + ' + ' + str(b) + ' = ' + str(summation)


def subtract(a, b):
  '''
  subtract two numbers and return the difference
  '''
  difference = round(a - b, 4)
  print('\nThe difference of ' + str(a) + ' and ' + str(b) + ' is ' + str(difference))
  return str(a) + ' - ' + str(b) + ' = ' + str(difference)


def multiply(a, b):
  '''
  multiply two numbers and return the product
  '''
  product = round(a * b, 4)
  print('\nThe product of ' + str(a) + ' and ' + str(b) + ' is ' + str(product))
  return str(a) + ' * ' + str(b) + ' = ' + str(product)


def divide(a, b):
  '''
  divide two numbers and return the quotient
  '''
  # perform the division if the denominator is not 0
  if b != 0:
    quotient = round(a / b, 4)
    print('\nThe quotient of ' + str(a) + ' and ' + str(b) + ' is ' + str(quotient))
    return str(a) + ' / ' + str(b) + ' = ' + str(quotient)
  # denominator is 0, results in error
  else:
    print('\nYou cannot divide by 0.')
    return 'DiV ERROR'


def exponent(a, b):
  '''
  take a number to a power and return the result
  '''
  power = round(a ** b, 4)
  print('\nThe result of ' + str(a) + ' raised to the ' + str(b) + ' power is ' + str(power))
  return str(a) + ' ^ ' + str(b) + ' = ' + str(power)


# the main code
print('Welcome to the Python Calculator App.')
print('\nEnter two numbers and an operation and the desired operation will be performed.')

history = []

running = True

while running:
  # get user input
  num1 = float(input('\nEnter a number: '))
  num2 = float(input('\nEnter a number: '))
  operator = input('\nEnter an operation\naddition(a), subtraction(s), multiplication(m), division(d), exponentiation(e) : ').strip().lower()

  # call the appropriate function based on the value of operator
  if operator == 'addition' or operator == 'a':
    result = add(num1, num2)
  elif operator == 'subtraction' or operator == 's':
    result = subtract(num1, num2)
  elif operator == 'multiplication' or operator == 'm':
    result = multiply(num1, num2)
  elif operator == 'division' or operator == 'd':
    result = divide(num1, num2)
  elif operator == 'exponentiation' or operator == 'e':
    result = exponent(num1, num2)
  else:
    print('That is not a valid operation. Try again.')
    result = 'OPP ERROR'

  # append the mathematical result to the history
  history.append(result)

  # allow user to quit
  choice = input('\nWould you like to run the program again? (y/n) : ').strip().lower()

  if choice != 'y':
    print('\nCalculation summary: ')
    for calc in history:
      print(calc)
    print('\nThank you for using Python Calculator app.')
    running = False