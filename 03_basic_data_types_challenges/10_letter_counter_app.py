print('Welcome!')
name = input('What is your name? ').title()
print('\nHello, ' + name + '.')
print('I will count the number of times that a specific letter occurs in a message.')
message = input('Please enter your message: ').lower()
letter = input('Which letter would you like to count the occurances of? ').lower()
count = message.count(letter)
# print(count)
# print(type(count))
print('\n' + name + ', your message has ' + str(count) + ' ' + letter + '(s) in it.')