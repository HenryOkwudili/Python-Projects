print("Price of the house is $1M")
print(
'''You will need to put down 10% if you have good credit, else,
   you will need to put down 20% if you have bad credit.''')

price = 1000000
good_price = (10/100)*price
bad_price = (20/100)*price

good_credit = True

if good_credit:
    print(f"You have good credit so put down 10%. Which is: ${good_price}")
else:
    print(f"You have bad credit so put down 20%. Which is: ${bad_price}")