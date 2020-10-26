import cmath

print('Welcome to the Quadratic Solver App.')

print('A quadratic equation is of the form: ax ^ 2 + bx + c = 0')
print('Your solution can be real or complex numbers.')
print('A complex number has two parts: a + bj')
print("Where 'a' is the real portion and 'bj' is the imaginary portion." )

# get user input
equations_number = int(input('\nHow many quadratic equations would you like to solve? : '))

# for-loop to go through each equation
for i in range(equations_number):
  print('\nSolving equation #' + str(i + 1))
  
  # solving the quadratic equation
  a = float(input("\nPlease enter the value of 'a' (coefficient of x^2): "))
  b = float(input("Please enter the value of 'b' (coefficient of x): "))
  c = float(input("Please enter the value of 'c': "))
  # solvin the quadratic formula
  x1 = - b + cmath.sqrt(((b ** 2) - (4 * a * c)) / 2 * a)
  x2 = - b + cmath.sqrt(((b ** 2) + (4 * a * c)) / 2 * a)

  print('\nEquation solved.')
  print('The solutions to ' + str(a) + ' x ^ 2' + str(b) + ' x ' + str(c) + ' are: ')
  print('\n\tx1 = ' + str(x1))
  print('\tx2 = ' + str(x2))

print('\nThank you for using the Quadratic Equation Solver!')