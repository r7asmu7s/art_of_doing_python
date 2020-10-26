# a class is a blueprint to build something.
# an object is what your build.
# an instance is what you work with once its built.
# an attribute is the information to distinguish one instance from another in a class.
# a method is a behavior which is common through all instances of a class (little functions)
# we need a method to initialize an object from the class when we call a method from a class

import random

class Baby():
  '''
  a simple class to simulate a baby.
  '''

  def __init__(self, name, gender, age):
    '''
    initialize attributes.
    '''
    self.name = name.title()
    self.gender = gender
    self.age = age
    self.tired = True
  
  def play(self):
    '''
    simulate playing based on gender.
    '''
    if self.gender == 'male':
      print(self.name + ' is playing with cars.')
    else:
      print(self.name + ' is playing with blocks.')
  
  def cry(self):
    '''
    simulate crying.
    '''
    print('WAAH WAAH WAHHH!!')
    print('Even ' + str(self.age) + ' year old cry.')
  
  def sleep(self):
    '''
    simulate sleeping
    '''
    if self.tired:
      print(self.name + ' is sleeping... FiNALLY!')
      self.tired = False
    else:
      print('Sorry! ' + self.name + ' is not tired.')

little_boy = Baby('john', 'male', 3)
little_girl = Baby('mary', 'female', 1)

print(little_boy.name + ' is a ' + str(little_boy.age) + ' year old ' + little_boy.gender + '.')
print(little_girl.name + ' is a ' + str(little_girl.age) + ' year old ' + little_girl.gender + '.')

little_boy.play()
little_girl.play()
little_boy.cry()
little_girl.cry()
little_boy.sleep()
little_girl.sleep()
little_boy.sleep()

babies = []
for i in range(100):
  num = random.randint(0, 1)
  if num:
    gender = 'female'
  else:
    gender = 'male'

  age = random.randint(0, 5)

  baby = Baby(str(i), gender, age)
  babies.append(baby)

for baby in babies:
  print('Baby #' + baby.name + ' is a ' + str(baby.age) + ' year old ' + baby.gender + '.')