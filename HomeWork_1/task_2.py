
balance = float(input("Please enter your balace:$"))
remaining_balance = balance * 100

QUATERS = 25
DIMES = 10
NICKLES = 5
PENNY = 1 

balance_of_quaters = remaining_balance // QUATERS 
print("Quaters:",balance_of_quaters)
remaining_of_quaters = remaining_balance % QUATERS

balance_of_dimes = remaining_of_quaters // DIMES
print ("Dimes", balance_of_dimes)
remaining_of_dimes = remaining_of_quaters % DIMES

balance_of_nickes = remaining_of_dimes // NICKLES
print ("Nickles:", balance_of_nickes)
remaining_of_nickeles = remaining_of_dimes % NICKLES

balance_of_pennies = remaining_of_nickeles / PENNY
remaining_of_pennies = remaining_of_nickeles % PENNY
print ("Pennies:", balance_of_pennies)
