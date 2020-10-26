colors = ['red', 'blue', 'green', 'yellow', 'blue']

print(colors)
colors.remove('yellow')
print(colors)

# .remove() method doesn't return any data 
colors.remove('blue')
print(colors)
colors.remove('blue')
print(colors)

new_colors = ['red', 'green', 'brown', 'orange']
removed_color = new_colors.pop()
print('Removing the color: ' + removed_color)

bad_color = new_colors.pop(1)
print('A bad color is: ' + bad_color)

print(colors)
del colors[0]
print(colors)

fruits = []
fruits.append(input('Enter a fruit: '))
fruits.append(input('Enter a fruit: '))
fruits.append(input('Enter a fruit: '))
print(fruits)