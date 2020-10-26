name = 'john'
fav_num = 13
tax_rate = 0.4
print(type(name))
print(type(fav_num))
print(type(tax_rate))

# str()
# int()
# float()

tax_rate = str(tax_rate)
print(type(tax_rate))

print(name.title() + "'s favorate number is " + str(fav_num) + ".")
print(type(fav_num))
print(name.title(), "'s favorite number is ", fav_num)

added_value = fav_num + 5
print(added_value)