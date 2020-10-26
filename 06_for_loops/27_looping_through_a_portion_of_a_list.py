numbers = list(range(1, 11))
for num in numbers:
  print(num)
print('\n')

# list slicing
for num in numbers[5:]:
  print(num)
print('\n')

# making a copy of a list
new_numbers = numbers
print(new_numbers)
print(numbers)

numbers.pop()
print(numbers)
print(new_numbers)
# both of these lists are referencing to the same object
print('\n')

numbers = list(range(1, 6))
print(numbers)
# properly copying a list
new_numbers = numbers[:]
print(numbers)
print(new_numbers)
numbers.pop()
print(numbers)
print(new_numbers)
print('\n')

# another way to copy a list
names = ['john', 'bill', 'mary']
new_names = names.copy()
print(names)
print(new_names)
new_names[0] = new_names[0].upper
print(names)
print(new_names)