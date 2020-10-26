print('Welcome to the Multiplication / Exponent Table App')

name = input('What is your name? ').title().strip()

number = float(input('Hello, ' + name + '. What number would you like to work with? '))

print('\nMultiplication Table for ' + str(number) + ': ')

print('\n\t1.0 * ' + str(number) + ' = ' + str(round(1 * number, 2)))
print('\t2.0 * ' + str(number) + ' = ' + str(round(2 * number, 2)))
print('\t3.0 * ' + str(number) + ' = ' + str(round(3 * number, 2)))
print('\t4.0 * ' + str(number) + ' = ' + str(round(4 * number, 2)))
print('\t5.0 * ' + str(number) + ' = ' + str(round(5 * number, 2)))
print('\t6.0 * ' + str(number) + ' = ' + str(round(6 * number, 2)))
print('\t7.0 * ' + str(number) + ' = ' + str(round(7 * number, 2)))
print('\t8.0 * ' + str(number) + ' = ' + str(round(8 * number, 2)))
print('\t9.0 * ' + str(number) + ' = ' + str(round(9 * number, 2)))

print('\nExponent Table for ' + str(number) + ': ')

print('\n\t' + str(number) + ' ** 1'  + ' = ' + str(round(number ** 1, 2)))
print('\t' + str(number) + ' ** 2'  + ' = ' + str(round(number ** 2, 2)))
print('\t' + str(number) + ' ** 3'  + ' = ' + str(round(number ** 3, 2)))
print('\t' + str(number) + ' ** 4'  + ' = ' + str(round(number ** 4, 2)))
print('\t' + str(number) + ' ** 5'  + ' = ' + str(round(number ** 5, 2)))
print('\t' + str(number) + ' ** 6'  + ' = ' + str(round(number ** 6, 2)))
print('\t' + str(number) + ' ** 7'  + ' = ' + str(round(number ** 7, 2)))
print('\t' + str(number) + ' ** 8'  + ' = ' + str(round(number ** 8, 2)))
print('\t' + str(number) + ' ** 9'  + ' = ' + str(round(number ** 9, 2)))

message = 'Math is Fun!'
print('\n' + message)
print('\t' + message.upper())
print('\t\t' + message.lower())
print('\t\t\t' + message.title())