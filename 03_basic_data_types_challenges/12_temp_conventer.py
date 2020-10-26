print('Welcom to the Temperature Conventer.')

fahrenheit = float(input('\nWhat is the given temperature in Fahrenheit degrees? '))
celsius = (fahrenheit - 32) * 5 / 9
celsius = round(celsius, 4)
kelvin = (fahrenheit + 569.67) * 5 / 9
kelvin = round(kelvin, 4)
print('\nThe given temperature is equal to:')
print('\nFahrenheit degrees: \t ' + str(fahrenheit))
print('Celsius degrees: \t ' + str(celsius))
print('Kelvin degrees: \t ' + str(kelvin))