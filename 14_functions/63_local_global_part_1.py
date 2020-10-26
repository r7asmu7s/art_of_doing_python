def times_ten(x):
  '''
  Multiply a number by 10
  '''
  print('Current value: ' + str(x))
  x *= 10
  print('Updated value: ' + str(x))
  return x

def char_replace(word):
  '''
  replace specific characters in a string with other characters.
  '''
  while 'a' in word:
    word = word.replace('a', '@')
  while 'e' in word:
    word = word.replace('e', '3')
  while 'i' in word:
    word = word.replace('i', '!')
  while 'o' in word:
    word = word.replace('o', '0')
  while 'u' in word:
    word = word.replace('u', '#')
  return word

number = 3
number = times_ten(number)
# print(x) # gives an error, becuase it's a local variable in the function
print(number)

phrase = 'hello, how are you doing today?'
print(phrase)
phrase = char_replace(phrase)
print(phrase)
# you should only makes changes to local variables inside the function
# you should not makes any changes to global variables inside the function
# you should not make any changes to local variables outside the function
# we can use return in the function to update our global variable
