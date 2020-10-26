print('Welcome to the Average Calculator App.')

# get user input
name = input('\nWhat is your name? : ').title().strip()
count = int(input('How many grades would you like to enter? : '))

# get user's grades
grades = []

for i in range(1, count + 1):
  grades.append(int(input('Enter grade : ')))

# sort grades and printing them
grades.sort(reverse=True)

print('\nGrades highest to lowest: ')
for grade in grades:
  print('\t' + str(grade))

# calculations
average = (sum(grades) / count) # instead of count we could use len(grades)
average = round(average, 2)

print('\n' + name + "'s grade summary: ")
print('\tTotal number of grades: ' + str(count))
print('\tHighest grade: \t\t' + str(max(grades)))
print('\tLowest grade: \t\t' + str(min(grades)))
print('\tAverage: \t\t' + str(average))

desired_average = float(input('\nWhat is your desired average? : '))

next_assignment = ( (count + 1) * desired_average) - sum(grades)

next_assignment = round(next_assignment, 2)

# print the summary

print('\nGood luck, ' + name + '!')
print('You need to get a ' + str(next_assignment) + ' on your next assignment to earn a ' + str(desired_average) + ' average.')

# make a copy of list of grades, swap out one of the grades

new_grades = grades[:] # or we can use grades.copy()

print("\nLet's see what your average could have been if you did better / worse on an assignment.")
which_grade = int(input('What grade would you like to change? : '))
new_which_grade = int(input('What grade would you like to change ' + str(which_grade) + ' to? : '))

new_grades.remove(which_grade)
new_grades.append(new_which_grade)

# sort new grades and printing them
new_grades.sort(reverse=True)

print('\nNew grades highest to lowest: ')
for grade in new_grades:
  print('\t' + str(grade))

# calculations
new_average = (sum(new_grades) / count) # instead of count we could use len(grades)
new_average = round(new_average, 2)

# new grades summary
print('\n' + name + "'s new grade summary: ")
print('\tTotal number of grades: ' + str(count))
print('\tHighest grade: \t\t' + str(max(new_grades)))
print('\tLowest grade: \t\t' + str(min(new_grades)))
print('\tAverage: \t\t' + str(new_average))

print('\nYour new average would be a ' + str(new_average) + ' compared to your real average which is ' + str(average) + '!')
print('That is a change of ' + str(round(abs(average - new_average), 2)) + ' points!')

print('\nToo bad your original grades are still the same!')
print(grades)
print('You should go ask for extra credits.')