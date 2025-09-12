# Done in 10 minutes in https://www.programiz.com/python-programming/online-compiler/. It's rough around the edges, but it works. Just don't input stupid numbers and it's usable

borrowed = 3000                             # How much money was borrowed.
months = 3                                  # How many months to pay it back in full.
growth = 1.015                              # Percentage of growth in decimals + 1. Used to calculate the amount paid per month
debt = borrowed * growth                    # Something most USA students are in.
parcel = debt/months                        # How much to pay this month.
debt = debt - parcel                        # Like, really. Imagine being born in a extreme capitalist country. Sucks to suck.
totalVaryingPerMonth = parcel               # Total for the main for function, if paying varying amounts each month
totalAtOnce = borrowed * growth ** months   # Mostly for debug or if you want to earn more money? Idk, my grandma liked it better to pay me the same amount each month.
monthsLeft = months-1                       # Should be auto-explicative.
currency = "R$"                             # Input your currency like a string, to appear before the money (sucks to suck, if it should go after)

print(f'You have to pay {currency}{round(parcel, 2)} this month. {currency}{round(debt, 2)} remains to be payed out of {currency}{round(borrowed, 2)} There are {monthsLeft} months left.')

for i in range(months-1):
    debt = debt * growth
    parcel = debt/monthsLeft
    debt = debt - parcel
    monthsLeft -= 1
    totalVaryingPerMonth += parcel
    if monthsLeft > 1:
        print(f'You have to pay {currency}{round(parcel, 2)} this month. {currency}{round(debt, 2)} remains to be payed out of {currency}{round(borrowed, 2)}. There are {monthsLeft} months left.')
    elif monthsLeft == 1:
        print(f'You have to pay {currency}{round(parcel, 2)} this month. {currency}{round(debt, 2)} remains to be payed out of {currency}{round(borrowed, 2)}. There is {monthsLeft} month left.')
    elif monthsLeft == 0:
        print(f'You have to pay {currency}{round(parcel, 2)} this month. Your debt is {currency}0.00. This is the last payment.')
    else:
        print('Something went wrong.')
    

print('')
print(f'In case paying as the amounts above mentioned, the total will be: R${round(totalVaryingPerMonth, 2)}.')
print('')
print(f'Total if paying same amount each month: R${round(totalAtOnce, 2)}. Total/months: R${round(totalAtOnce/months, 2)}') # Couldn't be bothered to write an informative print. You can comment this line out, or you can comment the print above out and only use this. Your choice. Only use this if the person paying you wants to pay the same amount each month, but then again, you are earning more this way. Let them know.
