print('Welcome to the Miles per Hour Converter App.')

speed_mph = float(input('\nWhat is your speed in miles per hour? '))

speed_mps = speed_mph * 1609.344 / 3600

print('\nYour speed in meters per second is ' + str(round(speed_mps, 2)) + ' .')