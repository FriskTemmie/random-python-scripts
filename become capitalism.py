# Done in 10 minutes in https://www.programiz.com/python-programming/online-compiler/. It's rough around the edges, but it works. Just don't input stupid numbers and it's usable

borrowed = 3000                # How much money was borrowed.
months = 3                     # How many months to pay it back in full.
growth = 1.015                 # Percentage of growth in decimals + 1. Used to cal
debt = borrowed * growth       # Something most USA students are in.
parcel = debt/months           # How much to pay this month.
debt = debt - parcel           # Like, really. Imagine being born in a extreme capitalist country. Sucks to suck.
total = borrowed * growth      # Mostly for debug or if you want to earn more money? Idk, my grandma liked it better to pay me the same amount each month.
monthsLeft = months-1          # Should be auto-explicative.

print(f'You have to pay R${round(parcel, 2)} this month. R${round(debt, 2)} remains to be payed out of {round(borrowed, 2)} There are {monthsLeft} months left.')

for i in range(months-1):
    debt = debt * growth
    parcel = debt/monthsLeft
    debt = debt - parcel
    total = total * growth
    monthsLeft = monthsLeft-1
    print(f'You have to pay R${round(parcel, 2)} this month. R${round(debt, 2)} remains to be payed out of {round(borrowed, 2)}. There are {monthsLeft} months left.')
    
print(f'Total: {round(total, 2)}. Total/months: {round(total/months, 2)}') # Couldn't be bothered to write an informative print. You can comment this line out if, or you can comment the print above out and only use this. Your choice.
