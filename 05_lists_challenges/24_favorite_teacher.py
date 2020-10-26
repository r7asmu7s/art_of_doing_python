print('Welcome to the Favorite Teachers Program')

# input of teachers' names
teachers = [] 
teachers.append(input('\nWho is your first favorite teacher? : ').strip().title())
teachers.append(input('Who is your second favorite teacher? : ').strip().title()) 
teachers.append(input('Who is your third favorite teacher? : ').strip().title())
teachers.append(input('Who is your forth favorite teacher? : ').strip().title())

# summary
print('\nYour favorite teachers ranked are: ' + str(teachers))
print('Your favorite teachers alphabetically ordered are: ' + str(sorted(teachers, reverse=True)))
print('Your favorite teachers alphabetically reverse ordered are: ' + str(sorted(teachers)))

print('\nYour top two teachers are: ' + teachers[0] + ' and ' + teachers[1] + '.')
print('Your next two favorite teachers are: ' + teachers[2] + ' and ' + teachers[3] + '.')
print('Your least favorite teacher is: ' + teachers[-1] + '.')
print('You have a total of ' + str(len(teachers)) + ' teachers.')

# insert a new favorite teacher
print('\nCalculating...')
teachers.insert(0, input('Oops, ' + teachers[0] + ' is no longer your first favorite teacher.\nWho is your new FAVORiTE teacher? : ').strip().title())

# summary
print('\nYour favorite teachers ranked are: ' + str(teachers))
print('Your favorite teachers alphabetically ordered are: ' + str(sorted(teachers, reverse=True)))
print('Your favorite teachers alphabetically reverse ordered are: ' + str(sorted(teachers)))

print('\nYour top two teachers are: ' + teachers[0] + ' and ' + teachers[1] + '.')
print('Your next two favorite teachers are: ' + teachers[2] + ' and ' + teachers[3] + '.')
print('Your least favorite teacher is: ' + teachers[-1] + '.')
print('You have a total of ' + str(len(teachers)) + ' teachers.')

# remove a specific teacher
teachers.remove(input("\nYou've decided that you no longer like a teacher. Which teacher would you like to remove from your list? : ").strip().title())

# summary
print('\nYour favorite teachers ranked are: ' + str(teachers))
print('Your favorite teachers alphabetically ordered are: ' + str(sorted(teachers, reverse=True)))
print('Your favorite teachers alphabetically reverse ordered are: ' + str(sorted(teachers)))

print('\nYour top two teachers are: ' + teachers[0] + ' and ' + teachers[1] + '.')
print('Your next two favorite teachers are: ' + teachers[2] + ' and ' + teachers[3] + '.')
print('Your least favorite teacher is: ' + teachers[-1] + '.')
print('You have a total of ' + str(len(teachers)) + ' teachers.')