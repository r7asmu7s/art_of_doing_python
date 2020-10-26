print('Welcome to the Binary / Hexadecimal Converter')

# get user input and generate lists
max_value = int(input('\nCompute binary and hexadecimal values up to the following decimal number: '))
decimals = list(range(1, max_value + 1))
binaries = []
hexadecimals = []

for decimal in decimals:
  binaries.append(bin(decimal))
  hexadecimals.append(hex(decimal))

print('\nGenerating output...\nCompleted.')
# get slicing index from user
print('\nUsing slices, we will now show a portion of each list.')
lower_range = int(input('What decimal number would you like to start at? : '))
upper_range = int(input('What decimal number would you like to stop at? : '))

# slice through each list individually
print('\nDecimal values from ' + str(lower_range) + ' to ' + str(upper_range) + '.')
for decimal in decimals[lower_range - 1:upper_range]:
  print(decimal)

print('\nBinary values from ' + str(lower_range) + ' to ' + str(upper_range) + '.')
for binary in binaries[lower_range - 1:upper_range]:
  print(binary)

print('\nHexadecimal values from ' + str(lower_range) + ' to ' + str(upper_range) + '.')
for hexadecimal in hexadecimals[lower_range - 1:upper_range]:
  print(hexadecimal)

# output the whole list to the screen
input('\nPress Enter to see all values from 1 to ' + str(max_value) + '.')
print('Decimal\t\tBinary\t\tHexadecimal')
for decimal, binary, hexadecimal in zip(decimals, binaries, hexadecimals):
  print(str(decimal) + '\t\t' + str(binary) + '\t\t' + str(hexadecimal))