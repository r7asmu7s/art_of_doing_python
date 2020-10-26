teams = ['giants', 'bills', 'jets', 'patriots']
print(teams)
print(type(teams))

# print(teams[0].title())
# print(teams[1].title())
# print(teams[2].title())
# print(teams[3].title())

for team in teams:
  print(team.title())
  print("You're goint to win the Super Bowl!\n")

print('Go football!')

values = [1, 2, 3, 4, 5]
total_sum = 0

for value in values:
  total_sum += value

print(f'\n{total_sum}')

triples = [['a','b', 'c'], ['1', '2', '3'],['do', 're', 'me']]

for list_value in triples:
  for elements in list_value:
    print(elements, end=' ')
  print('I just finished one the inner loops!')
print('Now I am outside both for-loops!')