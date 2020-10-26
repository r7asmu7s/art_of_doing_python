class House():
  '''
  a class to model a house that is for sale.
  '''
  def __init__(self, style, sq_foot, year_built, price):
    '''
    initialize attributes.
    '''
    self.style = style
    self.sq_foot = sq_foot
    self.year_built = year_built
    self.price = price

    self.sold = False
    self.weeks_on_market = 0

  def display_info(self):
    '''
    display the information on the house.
    '''
    print('\n-----House for Sale!-----')
    print('House Style:\t' + self.style)
    print('Square Feet:\t' + str(self.sq_foot))
    print('Year Built:\t' + str(self.year_built))
    print('Sale Price:\t' + str(self.price))
    print('\nThis house has been on the market for ' + str(self.weeks_on_market) + ' weeks.')

  def sell_house(self):
    '''
    sell the house.
    '''
    if self.sold == False:
      print('Congrats! Your house has been sold for $' + str(self.price) + '.')
      self.sold = True
    else:
      print('Sorry, this house is no longer for sale.')

  def change_price(self, amount):
    '''
    change the sale price of the house.
    '''
    self.price += amount
    if amount < 0:
      print('Price drop!!')
    else:
      print('The house has increased in value by $' + str(amount) + '.')

  def update_weeks(self, weeks = 1):
    '''
    increament the number of the weeks a house has been on the market.
    '''
    self.weeks_on_market += weeks

my_house = House('Ranch', 1800, 1962, 199000)

# print out the attributes of the house
print(my_house.style)
print(my_house.sq_foot)
print(my_house.year_built)
print(my_house.price)
print(my_house.sold)
print(my_house.weeks_on_market)

my_house.display_info()

# house on market for 1 week
my_house.update_weeks()
my_house.display_info()

# house on market for 15 week
my_house.update_weeks(15)
my_house.display_info()

# change the sale price
my_house.change_price(-15000)
my_house.display_info()

# house on market for 5 weeks
my_house.update_weeks(5)
my_house.display_info()

# new interest
my_house.change_price(10000)
my_house.display_info()

# wrong square footage
my_house.sq_foot -= 150
my_house.change_price(-1000)
my_house.display_info()

# sell house
my_house.sell_house()

# someone else wants to buy the house
my_house.sell_house()
