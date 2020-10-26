def get_info():
  '''
  get user information in a dictionary that represents a bank account.
  '''
  print('Welcome to the PYTHON NATiONAL BANK.')
  # get user input
  name = input('\nWhat is your name? : ').title().strip()
  savings = int(input('How much money would you like to set up your savings account with? : '))
  checking = int(input('How much money would you like to set up your checking account with? : '))

  # build a dictionary that represents a specific bank account
  bank_account = {
    'Name': name,
    'Savings': savings,
    'Checking': checking,
  }

  return bank_account

def make_deposit(bank_account, account, money):
  '''
  add money to a specific type of account.
  '''
  bank_account[account] += money
  print('\nDeposited $' + str(money) + ' into ' + bank_account['Name'] + "'s" + account.lower() + ' account.')
  

def make_withdrawal():
  '''
  withdraw money from a specific type of account.
  '''
  # checking that the balance will still be positive after the withdrawal
  if bank_account[account] - money >= 0:
    bank_account[account] -= money
    print('\nWithdrew $' + str(money) + ' from ' + bank_account['Name'] + "'s" + account.lower() + ' account.')
  else:
    print('\nSorry, by withdrawing $' + str(money) + ' you will have a negative balance.')

def display_info():
  '''
  display all key-value pairs in a given bank account.
  '''
  print('\nCurrent account information:')
  for key, value in bank_account.items():
    if key == 'Name':
      print(key + ': ' + str(value))
    else:
      print(key + ': $' + str(value))

# main code
# create a bank account
my_account = get_info()

running = True
while running:
  # show current state of the bank account
  display_info(my_account)

  # get user input for the transaction information
  account_type = input('\nWhat type of account would you like to access? (SAViNGS/CHECKiNG): ').title()
  choice = input('What type of transaction would you like to make? (DEPOSiTE/WiTHDRAWAL): ').title()
  amount = float(input('How much money for the transaction? : '))

  # make the correct function call based off previous user input
  if account_type == 'Savings' or account_type == 'Checking':
    if choice == 'Deposite':
      make_deposit(my_account, account_type, amount)
    elif choice == 'Withdrawal':
      make_withdrawal(my_account, account_type, amount)
    else:
      print('\nWe cannot do that for you today.')
  
  else:
    print('\nWe cannot do that for you today.')

  # allow user to make another transaction

  choice = input('\nWould you like to make another transaction? (Y/N): ').lower()
  if not choice.startswith('y'):
    display_info(my_account)
  else:
    print('\nHave a great day.')
    running = False