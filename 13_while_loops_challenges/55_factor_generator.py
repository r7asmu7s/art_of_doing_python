print('Welcome to the Factor Gernerator App')

running = True

# run the program until user quits

while running:
    # get user input
    number = int(
    input('\nEnter a number to determine all factors of that number: ').strip())

    # find the factors of the user's given number
    factors = []

    print('\nFactors of ' + str(number) + ' are:')

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    # print out the factors
    for factor in factors:
        print(factor)

    # print a summary of the factors mathematically
    print('\nIn summary: ')

    for i in range(int(len(factors) / 2)):
        print(str(factors[i]) + ' * ' + str(factors[-i - 1]) + ' = ' + str(number))

    # ask the user if they would like to quit
    choice = input('\nRun again? (y / n): ').lower()
    if choice != 'y':
        running = False
        print('Thank you for using the program.')