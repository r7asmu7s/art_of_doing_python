from collections import Counter

print('Welcome to the FREQUENCY ANALYSiS APP.')

non_letters = [' ', '.', ',', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '=', "'", '"', '1', '2', '3', '4', '5', '6','7', '8', '9', '0', '\n', '\t']

key_phrase_1 = input('\nEnter a word or phrase to count the occurence of each letter: ').lower()

for non_letter in non_letters:
  key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurances = len(key_phrase_1)

letter_count = Counter(key_phrase_1)

print('\nHere is the frequency analysis of the key phrase 1: ')
print('\n\tLetter:\t\tOccurence:\tPercentage:')

# frequency
for key, value in sorted(letter_count.items()):
  percentage = 100 * value / total_occurances
  percentage = round(percentage, 2)
  print('\t' + key + '\t\t' + str(value) + '\t\t' + str(percentage) + '%')

# make a list of letters from highest occurence to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []

for pair in ordered_letter_count:
  key_phrase_1_ordered_letters.append(pair[0])

# print the list
print('\nLetters ordered from highest occurence to lowest: ')
for letter in key_phrase_1_ordered_letters:
  print(letter, end='')

'''
PART II
'''

key_phrase_2 = input('\n\n\nEnter a word or phrase to count the occurence of each letter: ').lower()

for non_letter in non_letters:
  key_phrase_2 = key_phrase_2.replace(non_letter, '')

total_occurances = len(key_phrase_2)

letter_count = Counter(key_phrase_2)

print('\nHere is the frequency analysis of the key phrase 2: ')
print('\n\tLetter:\t\tOccurence:\tPercentage:')

# frequency
for key, value in sorted(letter_count.items()):
  percentage = 100 * value / total_occurances
  percentage = round(percentage, 2)
  print('\t' + key + '\t\t' + str(value) + '\t\t' + str(percentage) + '%')

# make a list of letters from highest occurence to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_2_ordered_letters = []

for pair in ordered_letter_count:
  key_phrase_2_ordered_letters.append(pair[0])

# print the list
print('\nLetters ordered from highest occurence to lowest: ')
for letter in key_phrase_2_ordered_letters:
  print(letter, end='')