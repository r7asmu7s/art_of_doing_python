def calc_age(age, interval = 0):
  '''
  Determine a person's age after interval years.
  '''
  age += interval
  return age
  # the rest of the function stops after we reach the return

def course_info(course_name, student_number, credit_hours):
  '''
  Simulate a college course and return the summary as a dictionary.
  '''
  course = {
    'Course Name': course_name.title(),
    'Student Number': student_number,
    'Credit Hours': credit_hours,
  }
  return course

def drop_student(course):
  '''
  Simulate dropping a student from a specific course.
  '''
  course['Student Number'] -= 1
  print('Dorpping student from ' + course['Course Name'] + '.')

new_age = calc_age(33, 10)
print(new_age)

new_age = calc_age(29, 50)
print(new_age)

python = course_info('Python Programming', 32, 4)
for key, value in python.items():
  print(key + ':' + str(value))

drop_student(python)

for key, value in python.items():
  print(key + ':' + str(value))