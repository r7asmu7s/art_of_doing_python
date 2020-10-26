import time

print('Welcome to the PRiME NUMBER APP.')

flag = True

while flag:

  print('\nEnter 1 to determine if a specific number is prime.')
  print('Enter 2 to determine all prime numbers within a set range.')
  choice = int(input('Enter you choice, 1 or 2? : '))

  if choice == 1:
    if_prime = int(input('\nEnter a number to determin if it is a prime number or not: '))
    '''
    SOLUTiON 1
    '''
    # calculating if a given number is a prime number
    if if_prime > 1:
      for i in range(2, if_prime):
        if if_prime % i == 0:
          print(str(if_prime) + ' is not a prime number.')
          break
      else:
        print(str(if_prime) + ' is a prime number.')
      # https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
      # else statement is used with a for loop 
    else:
      print('That is not a valid input')
    '''
    SOLUTiON 2
    '''
    '''
    prime_status = True
    for i in range(2, if_prime):
      if if_prime % i == 0:
        prime_status = False
        break
    if prime_status:
      print(str(if_prime) + ' is a prime number.')
    else:
      print(str(if_prime) + ' is not a prime number.')
    '''

  elif choice == 2:
    lower_end = int(input('\nEnter the lower end of your range: '))
    upper_end = int(input('Enter the upper end of your range: '))

    primes = []

    # get the current time
    start_time = time.time()

    # calculating for a range of numbers to figure out whether it's a prime number or not
    '''
    SOLUTiON 1
    '''
    for i in range(lower_end, upper_end + 1):
      if i > 1:
        for n in range(2, i):
          if i % n == 0:
            break
        else:
          primes.append(i)
        # python documentation
        # https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
        # else statement is used with a for loop
    '''
    SOLUTiON 2
    '''
    '''
    for prime_candidate in range(lower_end, upper_end + 1):
      # i is not prime
      if prime_candidate > 1:
        prime_status = True
        for i in range(2, prime_candidate):
          if prime_candidate % i == 0:
            prime_status = False
            break
      else:
        prime_status = False
      
      # prime candidate is a prime number.
      if prime_status:
        primes.append(prime_candidate)
    '''

    # get the current time
    end_time = time.time()

    # determine the time of the calculations
    delta_time = round(end_time - start_time, 4)

    print('Calculations took a total of ' + str(delta_time) + ' seconds.')


    # output for the list of prime numbers
    print('The following numbers between ' + str(lower_end) + ' and ' + str(upper_end) + ' are prime.')
    input('Press enter to continue...')
    for prime in primes:
      print(prime)

  # unvalid choice
  else:
    print('That is not a valid option.')

  run_again = input('\nWould you like to run the program again? (Y/N): ').lower()

  if not run_again.startswith('y'):
    flag = False

print('\nThank you for using the program.')
