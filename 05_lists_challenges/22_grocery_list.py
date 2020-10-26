import datetime 

# create the datetime object and store the current date and time.
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

# the challenge itself:
grocery = ['Meat', 'Cheese']

print('\nWelcome to the Grocery List App.')
print('Current Date and Time is: ' + month + '/' + day + '\t' + hour + ':' + minute + '.')
print('You currently have ' + str(grocery[0]) + ' and ' + str(grocery[1]) + ' in your list.')

# adding grocery to the list
grocery.append(input('\nWhat type of food to add to the grocery list? ').title())
print('\nHere is your grocery list:')
print(grocery)
grocery.append(input('What type of food to add to the grocery list? ').title())
print('\nHere is your grocery list:')
print(grocery)
grocery.append(input('What type of food to add to the grocery list? ').title())

print('\nHere is your grocery list:')
print(grocery)
print('Here is your grocery list sorted:')
grocery.sort()
print(grocery)

print('\nSimulating grocery shopping...')

# removing items from the list
print('\nCurrent grocery list: ' + str(len(grocery)) + ' items.')
print(grocery)
removed_item = input('\nWhat food did you just purchased? ').title()
grocery.remove(removed_item)
print('Removing ' + removed_item + ' from the list...')

print('\nCurrent grocery list: ' + str(len(grocery)) + ' items.')
print(grocery)
removed_item = input('\nWhat food did you just purchased? ').title()
grocery.remove(removed_item)
print('Removing ' + removed_item + ' from the list...')

# unavailable item
print('\nCurrent grocery list: ' + str(len(grocery)) + ' items.')
print(grocery)
removed_item = input('\nWhat food did you just purchased? ').title()
grocery.remove(removed_item)
print('Removing ' + removed_item + ' from the list...')
print('\nCurrent grocery list: ' + str(len(grocery)) + '.')
print(grocery)
print('\nStore update: Sorry, the store is out of ' + str(grocery[-1]) + '.')
grocery.pop()

grocery.insert(0, input('What food would you like add intead? ').title())

print('Here is what remains on your grocery list:')
grocery.sort()
print(grocery)