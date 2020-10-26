names = []
print(names)
print(bool(names))

names.append('mike')
print(names)
print(bool(names))

print(0)
print(bool(0))
print(1)
print(bool(1))

print(bool(44))

numbers = list(range(1, 11))
print(numbers)

while numbers:
  numbers.pop()
  print(numbers)
print('All elements removed.')

numbers = [4, 1, 2, 3, 4, 4, 4, 5, 6, 4, 7, 4, 8, 4]
while 4 in numbers:
  numbers.remove(4)
  print(numbers)
print('All 4s removed.')

flag_1 = True
flag_2 = True

while flag_1:
  print('While loop #1 is running...')
  while flag_2:
    print('While loop #2 is running...')
    choice = input('Continue running while loop #2 ? : (y/n)')
    if choice.lower != 'y':
      flag_2 = False
      print('Ending while loop #2...')
  choice = input('Continue running while loop #1 ? : (y/n)')
  if choice.lower() != 'y':
    flag_1 = False
    print('Ending while loop #2...')