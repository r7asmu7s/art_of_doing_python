print(4 / 2)
print(4 % 2)

print(8 / 5)
print(8 % 5)

print(10 % 4)

current_num = 1

while current_num <= 10:
  if current_num % 2 == 0:
    print(str(current_num) + ' is even!')
  else:
    print(str(current_num) + ' is odd!')
  current_num += 1

flag = True
current_num = 1
while flag:
  if current_num % 3 == 0:
    print(str(current_num) + ' is divisible by 3!')
  else:
    print(str(current_num) + ' is not divisible by 3!')
  
  choice = input("Enter 'n' to stop or press 'Enter' to continue: ")
  if choice.lower() == 'n':
    # flag = False
    break

  current_num += 1

print(current_num)
print('Quitting...')

num = 10
while num > 0:
  num -= 1
  if num % 4 == 0:
    continue
  print('Current variable value: ' + str(num))

print('All Done!')