#Done in 10 minutes in https://www.programiz.com/python-programming/online-compiler/. It's rough around the edges, but it works. Just don't input stupid numbers and it's usable

borrowed = 3000 # How much money was borrowed
months = 3 # How many months to pay it back in full
growth = 1.015 # Percentage of growth in decimals + 1
debt = borrowed * growth
parcel = debt/months
debt = debt - parcel
total = borrowed * growth
monthsLeft = months-1
print(f'You have to pay R${round(parcel, 2)} this month. R${round(debt, 2)} remains to be payed out of {round(borrowed, 2)} There are {monthsLeft} months left.')

for i in range(months-1):
    debt = debt * growth
    parcel = debt/monthsLeft
    debt = debt - parcel
    total = total * growth
    monthsLeft = monthsLeft-1
    print(f'You have to pay R${round(parcel, 2)} this month. R${round(debt, 2)} remains to be payed out of {round(borrowed, 2)}. There are {monthsLeft} months left.')
print(f'Total: {round(total, 2)}. Total/months: {round(total/months, 2)}')
