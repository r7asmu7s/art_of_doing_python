values = range(1, 10)
print(values)
print(type(values))

for i in range(1, 11):
  print(i)

for num in range(5): # the default starting value is zero
  print(num)

for i in range(2, 11, 2): # the third value is optional, it sets the step
  print(i)

word = 'Hello World'
list_word = list(word)
print(word)
print(list_word)

list_word[5] = 'NEW'
print(list_word)

# new_word = 'hi'.join(list_word)
new_word = ''.join(list_word)
print(new_word)

numbers = list(range(10, 101, 10))

for number in numbers:
  print(number)

squares = []
for num in numbers:
  square = num ** 2
  squares.append(square)

print('Populating squares complete!')

for square in squares:
  print(square)

# list comprehension !important
cubes = [num ** 3 for num in numbers]
for cube in cubes:
  print(cube)

print(min(cubes))
print(max(cubes))
print(sum(cubes))