fav_colors = {
  'john': 'blue',
  'gabe': 'orange',
  'mary': 'yellow',
  'mike': 'purple',
  'lucas': 'yellow',
  'sarah': 'green',
}

print(fav_colors)

# .item() method returns a list of tuples set of keys and values
fav_colors_list = fav_colors.items()
print(fav_colors_list)

for key, value in fav_colors.items():
  print('The key ' + key + ' has an associated value of ' + value + '.')

# the .key() method return a list of keys of the dictionary
fav_colors_keys = fav_colors.keys()
print(fav_colors_keys)

for key in fav_colors.keys():
  print(key.title() + ', thank you for taking the survey.')

if 'broke' not in fav_colors.keys():
  print('Brook, you should take the survey.')

# the .values() method returns a list of values of the dictionary
fav_colors_values = fav_colors.values()
print(fav_colors_values)

for value in fav_colors.values():
  print(value)

# the set function removes the repeated values of the dictionary
print('\nThe colors voted on were: ')
for value in set(fav_colors.values()):
  print(value)