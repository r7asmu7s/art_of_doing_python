import math

print('Welcome to the Right Triangle Solver App.')
print('\nThe measure of two legs of the triangle is needed.')

first_leg = float(input('What is the first leg of the triangle? '))
# first_leg = round(first_leg, 2)
second_leg = float(input('What is the second leg of the triangle? '))
# second_leg = round(second_leg, 2)

hypo = (first_leg ** 2) + (second_leg ** 2)
hypo = math.sqrt(hypo)
# hypo = hypo ** (1/2)
hypo = round(hypo, 3)

area = (first_leg * second_leg) / 2
area = round(area, 3)

print('\nFor a triangle with legs of ' + str(first_leg) + ' and ' + str(second_leg) + ': ')
print('The hypotenuse is ' + str(hypo) + ' .')
print('The area is ' + str(area) + ' .')