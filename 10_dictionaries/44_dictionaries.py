bob_info = {
  'first_name': 'Bob',
  'last_name': 'Jones',
  'age': 27,
  'fav_colors': ['green', 'orange'],
}

print(bob_info)
print(type(bob_info))

print(bob_info['age'])
print(bob_info['fav_colors'])
print(bob_info['fav_colors'][0])

bob_info['weight'] = 180
bob_info['height'] = 72.6
print(bob_info)

bob_info['weight'] -= 5
print('Wow ' + bob_info['first_name'] + ', you lost some weight. You now weight ' + str(bob_info['weight']) + ' pounds.')

bob_info['age'] += 1
print('Happy birthday ' + bob_info['first_name'] + '! You are now ' + str(bob_info['age']) + ' years old.')

del bob_info['fav_colors']
print(bob_info)

user_info = {}
user_info['name'] = input('What is your name? : ').title()
user_info['age'] = input('What is your age? :')
user_info['job'] = input('Enter your job title: ').title()
print(user_info)