# parent class ----> child class

# the parent class
class Dog():
  '''
  a class to represent a general dog.
  '''
  def __init__(self, name, gender, age, loud):
    '''
    initialize attributes.
    '''
    self.name = name.title()
    self.gender = gender
    self.age = age
    self.is_loud = loud # loud is a boolean

  def call_dog(self):
    '''
    call the dog.
    '''
    if self.gender == 'male':
      print('Here ' + self.name + '! Good boy!')
    else:
        print('Here ' + self.name + '! Good girl!')
  
  def dog_years(self):
    '''
    compute age in dog years.
    '''
    dog_years = self.age * 7
    print(self.name + ' is ' + str(dog_years) + ' years old in dog years.')

  def bark(self):
    '''
    get the dog to speak.
    '''
    if self.is_loud:
      print('Woof woof woof!')
    else:
      print('Woof...')


# a chile class - beagle
class Beagle(Dog):
  '''
  a class to represent a specific type of dog.
  '''
  def __init__(self, name, gender, age, loud, gunshy):
    '''
    initialize attributes of the parents class.
    '''
    # another way to initialize the child class
    # Dog.__init__(self, ...)

    super().__init__(name, gender, age, loud)
    self.is_gunshy = gunshy #a boolean
  
  def go_hunt(self):
    '''
    if the dog is not gun shy, take them hunting.
    '''
    if not self.is_gunshy:
      self.bark()
      print(self.name + ' just brought back a duck.')
    else:
      print(self.name + ' is not a good hunting dog.')

  def bark(self):
    '''
    get the dog to speak.
    '''
    if self.is_loud:
      print('HOOOWWWLLL!')
    else:
      print('Howl...')


class Chihuahua(Dog):
  '''
  represents a specific type of dog.
  '''
  def __init__(self, name, gender, age, loud):
    '''
    initialize attributes from the parent class.
    '''
    Dog.__init__(self, name, gender, age, loud)

  def bark(self):
    if self.is_loud:
      print('Yip Yip Yip Yip Yip Yip Yip Yip !!')
    else:
      print('Yip...')


my_dog = Dog('spot', 'male', 3, True)

print(my_dog.name)
print(my_dog.age)

my_dog.call_dog()
my_dog.dog_years()
my_dog.bark()

my_beagle = Beagle('lassie', 'female', 8, False, False)

print(my_dog)
print(type(my_dog))
print(my_beagle)
print(type(my_beagle))

my_beagle.call_dog()
my_beagle.dog_years()
my_beagle.bark()

my_beagle.go_hunt()
my_beagle.bark()

tiny_dog = Chihuahua('tiny', 'male', 2, True)
tiny_dog.call_dog()
tiny_dog.dog_years()
tiny_dog.bark()
# tiny_dog.go_hunt() 'Chihuahua' object has no attribute 'go_hunt'