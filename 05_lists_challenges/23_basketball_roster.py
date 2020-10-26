print('Welcome to the Basketball Roster Program')

basketball_roster = []

point_guard = input('Who is your point guard? ').title()
basketball_roster.append(point_guard)
shooting_guard = input('Who is your shooting guard? ').title()
basketball_roster.append(shooting_guard)
small_forward = input('Who is your small forward? ').title()
basketball_roster.append(small_forward)
power_forward = input('Who is your power forward? ').title()
basketball_roster.append(power_forward)
center = input('Who is your center? ').title()
basketball_roster.append(center)

print('\n\tYour starting 5 for the upcomming basketball season')
print('\t\tPoint Guard:\t' + str(basketball_roster[0]))
print('\t\tShootin Guard:\t' + str(basketball_roster[1]))
print('\t\tSmall Forward:\t' + str(basketball_roster[2]))
print('\t\tPower Guard:\t' + str(basketball_roster[3]))
print('\t\tCenter:\t\t' + str(basketball_roster[4]))

print('\nOh no, ' + str(basketball_roster[2]) + ' is injured.')
print('Your roster only has ' + str(len(basketball_roster)-1) + ' players.')
basketball_roster[2] = input('Who will take ' + basketball_roster[2] + "'s spot? ").title()

print('\n\tYour starting 5 for the upcomming basketball season')
print('\t\tPoint Guard:\t' + str(basketball_roster[0]))
print('\t\tShootin Guard:\t' + str(basketball_roster[1]))
print('\t\tSmall Forward:\t' + str(basketball_roster[2]))
print('\t\tPower Guard:\t' + str(basketball_roster[3]))
print('\t\tCenter:\t\t' + str(basketball_roster[4]))

print('\nGood luck ' + str(basketball_roster[2] + ', you will do great!'))
print('Your roster now has ' + str(len(basketball_roster)) + ' players.')