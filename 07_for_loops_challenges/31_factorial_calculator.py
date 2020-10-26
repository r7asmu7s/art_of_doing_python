import math

print('Welcome to the Factorial Calculator App.')

# get user input
number = int(input('\nWhat number would you like to compute the factorial of? : '))

# display the mathematical relationship of a factorial
print(str(number) + '! = ', end='')
for i in range(1, number):
  print(str(i), end=' * ')
print(str(number))

# using the math library
fact = math.factorial(number)
print('\nHere is the result from the math library: ')
print('The factorial of ' + str(number) + ' is ' + str(fact) + '.')

# using my own algorithm
fact = 1
for i in range(1, number + 1):
  fact = fact * i
print('\nHere is the result from my own algorithm: ')
print('The factorial of ' + str(number) + ' is ' + str(fact) + '.')

# summary
print('\nIt is shown twice that ' + str(number) + '! = ' + str(fact) + '.')

'''
# my algorithm
number = int(input('\nWhat number would you like to calculate the factorial of? : '))
print(str(number) + '! = ', end='')
for i in reversed(range(1, number + 1)):
  if i != 1:
    print(str(i), sep=', ', end=' * ')
  else:
    print(str(i))
result = 1

print(str(number) + '! = ', end='')

for i in range(1, number + 1):
  result = result * i

print(result)
'''