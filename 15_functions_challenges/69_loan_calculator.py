from matplotlib import pyplot

def get_loan_info():
  '''
  get the basic information of a loan and store it in a dictionary.
  '''
  # create a blank dictionary to represent a loan
  loan = {}

  # get user input for the catagories of the loan
  loan['principal'] = float(input('\nEnter the loan amount: '))
  loan['rate'] = float(input('Enter the interest rate: ')) / 100
  loan['monthly payment'] = float(input('Enter the amount of desired monthly payment: '))
  loan['money paid'] = 0

  return loan


def show_loan_info(loan, number):
  '''
  display the current loan status.
  '''
  print('\n-----Loan Information after ' + str(number) + ' months-----')
  for key, value in loan.items():
    print(key.title() + ': ' + str(value))

def collect_interest(loan):
  '''
  update loan for interest per month.
  '''
  # divide by 12 to simulate collecting interest monthly
  loan['principal'] = loan['principal'] + loan['principal'] * loan['rate'] / 12

def make_monthly_payment(loan):
  '''
  simulate making a monthly payment to pay down the principal.
  '''
  loan['principal'] = loan['principal'] - loan['monthly payment']
  # you are required to make a full payment, you have not paid off your loan
  if loan['principal'] > 0:
    loan['money paid'] += loan['monthly payment']
  # you are not required to make a full payment, you have paid off your loan
  else:
    # for this else block, loan principal will be negative
    loan['money paid'] += loan['monthly payment'] + loan['principal']
    loan['principal'] = 0

def summarize_loan(loan, number, initial_principal):
  '''
  display the results of paying off the loan.
  '''
  print('\nCongratulations! You paid off your loan in ' + str(number) + ' months.')
  print('Your initial loan was $' + str(initial_principal) + ' at a rate of ' + str(loan['rate'] * 100) + '%.')
  print('Your monthly payment was $' + str(loan['monthly payment']) + '.')
  print('You spent $' + str(round(loan['money paid'], 2)) + ' in total.')
  
  # calculate money spent on interest
  interest = round(loan['money paid'] - initial_principal, 2)
  print('You spent $' + str(interest) + ' on interest!')


def create_graph(data, loan):
  '''
  create a graph to show relationship between principal and time.
  '''
  x_values = [] # represents month numbers
  y_values = [] # represents principal value

  # loop through data set, point is a tuple, point[0] represents month number, point[1] represents principal value.
  for point in data:
    x_values.append(point[0])
    y_values.append(point[1])

  # create a plot for x_values which is month number and y_values which is principal values
  pyplot.plot(x_values, y_values)
  pyplot.title(str(100 * loan['rate']) + '% interest with $' + str(loan['monthly payment']) + ' monthly payment.')
  pyplot.xlabel('Month Number')
  pyplot.ylabel('Principal of Loan')

  # display created graph
  pyplot.show()


# THE MAiN CODE
print('Welcome to the LOAN CALCULATOR APP.')

# initialize variables
month_number = 0
my_loan = get_loan_info()
starting_principal = my_loan['principal']
data_to_plot = []

# display starting conditions of loan
show_loan_info(my_loan, month_number)
input('Press Enter to begin paying off your loan.')

# simulate paying off the loan as long as the loan's principal > 0
while my_loan['principal'] > 0:
  # you cannot get ahead of the interest, you will never pay off the loan
  if my_loan['principal'] > starting_principal:
    break

  # it is possible to pay off the loan
  # increment month number, collect interest, make a payment, add data, and show loan info
  month_number += 1
  collect_interest(my_loan)
  make_monthly_payment(my_loan)
  data_to_plot.append((month_number, my_loan['principal']))
  show_loan_info(my_loan, month_number)

# the loan is either paid off in full or it can never be paid off.
# the loan is paid off in full
if my_loan['principal'] <= 0:
  summarize_loan(my_loan, month_number, starting_principal)
  create_graph(data_to_plot, my_loan)
# the loan can never be paid off, can't get ahead of interest
else:
  print('\nYou will NEVER pay off your loan!')
  print('You cannot get ahead of the interest.')