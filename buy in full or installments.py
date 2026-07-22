# Made in 06/04/2025. I put some effort into this, so it should work unless you try to break it. https://www.programiz.com/python-programming/online-compiler/

# TODO: Add option to not use the reserve
# TODO: Change discount values to percentage, and "installmentPrice" to the first/slash installment, aka the one that you pay more/less than the others
# TODO: Add option for fees (if 0, ignore)
reserve = 7578.17           # Money you have saved. Don't count the price of the product.
installments = 10           # Months to pay in payd in installments.
gainsPercent = 0.0118       # Your average gains per month in percentage (100% = 1).
installmentPrice = 74.99    # The price to pay (not total) in a installment.
noDiscoutPrice = 749.9      # The full price to pay, without discounts.
discount = 37.2             # The discount you get by paying in full. 

# If you buy in full.
ifFullReserve = reserve - (noDiscoutPrice - discount)
for i in range (installments):
    ifFullReserve = ifFullReserve + (ifFullReserve * gainsPercent)
    #print(ifFullReserve)
print(f'Money after {installments} months if full: {ifFullReserve}')

# If you buy in installments.
for i in range (installments):
    reserve = reserve + (reserve * gainsPercent)
    reserve = reserve - installmentPrice
print(f'Money after {installments} months if installments: {reserve}')

if reserve > ifFullReserve:
    print(f'Buy in installments. Difference: {reserve - ifFullReserve}')
elif reserve < ifFullReserve:
    print(f'Buy in full. Difference: {ifFullReserve - reserve}')
elif reserve == ifFullReserve:
    print(f'Both reserves are equal. There\' either no discount, or you did something wrong.')
else:
    print('Something went wrong.')
