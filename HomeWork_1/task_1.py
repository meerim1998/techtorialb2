num_quaters = input ("Number of Quoaters:")
quaters = 25 * int(num_quaters) / 100
print(quaters)

num_dimes = input("Number of Dimes:")
dimes = 10 * int(num_dimes) / 100
print (dimes)

num_nickels = input("Number of Nickles:")
nickels = 5 * int(num_nickels) / 100
print(nickels)

num_penny = input("Number of Penny:")
penny = 1 * int (num_penny) / 100
print(penny)

total = round(quaters + dimes + nickels + penny, 2)
print ("The total in dollars is$",total)





