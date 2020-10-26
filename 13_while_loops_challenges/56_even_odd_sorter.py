print('Welcome to the EVEN/ODD NUMBER SORTER.')

flag = True


while flag:
  numbers_string = input('\nEnter in a string of numbers seperated by a comma (,): ')
  numbers_string = numbers_string.replace(' ', '')

  numbers_list = numbers_string.split(',')

  # converting the strings in the list to integers
  # using list comprehension
  numbers_list = [int(x) for x in numbers_list]
  # using for loop
  # for number in numbers_list:
  #   number = int(number)
  # then we continue with for loop to print the result

  odds = []
  evens = []

  print('-----RESULT SUMMARY-----')
  for i in numbers_list:
    if i % 2 == 0:
      evens.append(i)
      print('\t' + str(i) + ' is an even number.')
      
    else:
      odds.append(i)
      print('\t' + str(i) + ' is an odd number.')

  odds = sorted(odds)
  # odds.sort()
  evens = sorted(evens)
  # evens.sort()

  print('\nThe folowing ' + str(len(evens)) + ' numbers are even:')
  for number in evens:
    print('\t' + str(number))

  print('\nThe folowing ' + str(len(odds)) + ' numbers are odd:')
  for number in odds:
    print('\t' + str(number))

  choice = input('\nWould you like to run the program again? (y/n): ').lower()

  if not choice.startswith('y'):
    flag = False

print('\nThank you for using the program.')