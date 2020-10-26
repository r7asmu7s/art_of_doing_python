sports = ['baseball', 'golf', 'soccer', 'football']
print(sports)

# sorted() function does only make changes temporarily
print(sorted(sports))
print(sports)
print(sorted(sports, reverse=True))
print(sports)

grades = [88, 74, 95, 100, 92]
print(grades)
print(sorted(grades))
print(sorted(grades, reverse=True))
print(grades)

# sorted_grades = sorted(grades)
# print(sorted_grades)

grade_length = len(grades)
print(grade_length)
print(type(grade_length))

removed_grade = grades.pop()
print('Removing grade: ' + str(removed_grade))
print(len(grades))

# .sort() and .reverse() method change the list permanently and are not temporary

print(sports)
sports.sort()
print(sports)

print(grades)
grades.sort(reverse=True)
print(grades)

print(sports)
sports.reverse()
print(sports)

# sorting is different based on lower or upper case of first letters.