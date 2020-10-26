print('Welcome to the Grade Sorter App')

first_grade = int(input('\nWhat is your first grade? (0-100) : '))
second_grade = int(input('What is your second grade? (0-100) : '))
third_grade = int(input('What is your third grade? (0-100) : '))
forth_grade = int(input('What is your forth grade? (0-100) : '))

grades = [first_grade, second_grade, third_grade, forth_grade]

print('\nYour grades are: ' + str(grades))

grades.sort(reverse=True)

print('\nYour grades from highest to lowest are: ' + str(grades))

print('\nThe lowest two grades will now be dropped.')
removed_grade = grades.pop()
print('Removed grade: ' + str(removed_grade))
removed_grade = grades.pop()
print('Removed grade: ' + str(removed_grade))

print('\nYour remaining grades are: ' + str(grades))
print('Nice work! Your highest grade is' + str(grades[0]) + '.')