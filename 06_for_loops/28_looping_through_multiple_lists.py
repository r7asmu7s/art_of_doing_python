names = ['jack', 'john', 'mark', 'bill']
numbers = [20, 44, 3, 14]

# for name in names:
#   print(name)

# for number in numbers:
#   print(number)

for i in range(len(names)):
  print(names[i].title() + ': ' + str(numbers[i]))

# the zip function
for name, number in zip(names, numbers):
  print(name.title() + ': ' + str(number))