def remove_names(names):
  '''
  Remove a name from a list.
  '''
  removed_name = names.pop()
  print('Goodbye ' + removed_name.title() + '.')
  return names

friends = ['john', 'jack', 'jill', 'james']
print(friends)
new_friends = remove_names(friends.copy())
print(friends)
print(new_friends)

# def add_two(num):
#   '''
#   add 2 to a number.
#   '''
#   num += 2

# value = 10
# print(value)
# value = add_two(value)
# print(value)

# only lists and dictionaries are mutable here. integers are immutable.

# nums = [1, 2, 3, 4]
# # new_nums = nums
# new_nums = nums.copy()
# new_nums.append(5)
# print(nums)
# we are pointing to the same object