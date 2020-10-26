colors = ['red', 'orange', 'green']
print(colors)
print(colors[2])
print(colors[-1])
colors[2] = 'yellow'
print(colors)

colors.append('blue')
print(colors)

new_colors = []
new_colors.append('red')
new_colors.append('purple')
new_colors.append('blue')
print(new_colors)

print(new_colors[1])
new_colors.insert(1, 'brown')
print(new_colors[1])
print(new_colors)
new_colors.insert(3, 'red')
print(new_colors)