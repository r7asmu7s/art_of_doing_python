status = True
print(status)
print(type(status))

status = False
print(status)
print(type(status))

soda = 'coke'
print(soda == 'coke')
print(soda == 'pepsi')
print(soda == 'Coke')
print(soda != 'root beer')

names = ['mike', 'john', 'mary']
mike_status = 'mike' in names
bill_status = 'bill' in names
print(mike_status)
print(bill_status)
not_bill_status = 'bill' not in names
print(not_bill_status)