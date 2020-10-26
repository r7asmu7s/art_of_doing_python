# a class is a blueprint to build something.
# an object is what your build.
# an instance is what you work with once its built.
# an attribute is the information to distinguish one instance from another in a class.
# a method is a behavior which is common through all instances of a class (little functions)
# we need a method to initialize an object from the class when we call a method from a class


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
    pass
  
  def cry(self):
    pass
  
  def sleep(self):
    pass

little_boy = Baby('john', 'male', 3)
little_girl = Baby('mary', 'female', 1)

print(little_boy.name)
print(little_girl.name)

print(little_boy.gender)
print(little_girl.age)

print(little_boy.tired)