# for loops : running a set number of times
# while loops : running until a certain condition is met

for i in range(1, 11):
  print(i)

current_num = 1

while current_num <= 10:
  print(current_num)
  current_num += 1

current_num = 1
while True:
  print(current_num)
  current_num += 1
  choice = input("Press enter to print the next number or 'q' to quit : ").lower()
  if choice == 'q':
    break