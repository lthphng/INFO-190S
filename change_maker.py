nickel = 0
dime = 25
quarter = 0
one = 0
five = 0
epsilon = 0.0196/100

print('Welcome to the vending machine change maker program\nChange maker initialized.\nStock contains:')
print(f'\t{nickel} nickels\n\t{dime} dimes\n\t{quarter} quarters\n\t{one} ones\n\t{five} fives\n')
price = input("Enter the purchase price (xx.xx) or `q' to quit: ")

while price != 'q':
    price = float(price)
    while price*100%5 != 0:
        print('Illegal price: Must be a non-negative multiple of 5 cents.\n')
        price = input("Enter the purchase price (xx.xx) or `q' to quit: ")
        if price == 'q':
            break
        else:
            price = float(price)
    if price != 'q':
        print("\nMenu for deposits:\n\t'n' - deposit a nickel\n\t'd' - deposit a dime\n\t'q' - deposit a quarter\n\t'o' - deposit a one dollar bill\n\t'f' - deposit a five dollar bill\n\t'c' - cancel the purchase\n")
        while price > 0:
            if price > 1:
                print(f'Payment due: {price//1:.0f} dollars and {(price - price//1)*100:.0f} cents')
                deposit = input('Indicate your deposit: ')
            else:
                print(f'Payment due: {price * 100:.0f} cents')
                deposit = str(input('Indicate your deposit: '))

            if deposit != 'n' and deposit != 'd' and deposit != 'q' and deposit != 'o' and deposit != 'f' and deposit != 'c':
                print(f'Illegal selection: {deposit}')
            elif deposit == 'n':
                price -= 0.05
                nickel += 1
            elif deposit == 'd':
                price -= 0.1
                dime += 1
            elif deposit == 'q':
                price -= 0.25
                quarter += 1
            elif deposit == 'o':
                price -= 1
                one += 1
            elif deposit == 'f':
                price -= 5
                five += 1
            else:
                break
        print('\nPlease take the change below:')
        #Greedy algorithm
        returnCur = 0
        if price == 0:
            print('\tNo change due.')
        while (price <= -0.25 + epsilon or price <= -0.25 - epsilon) and quarter > 0:
            price += 0.25
            quarter -= 1
            returnCur += 1
        if returnCur > 1 or quarter >= 0:
            if quarter < 0:
                print(f'\t{returnCur - 1} quarters')
            elif returnCur != 0:
                print(f'\t{returnCur} quarters')
        if quarter < 0:
            quarter = 0
        returnCur = 0
        while (price <= -0.1 + epsilon or price <= -0.1 - epsilon) and dime > 0:
            price += 0.1
            dime -= 1
            returnCur += 1
        if returnCur > 1 or dime >= 0:
            if dime < 0:
                print(f'\t{returnCur - 1} dimes')
            elif returnCur != 0:
                print(f'\t{returnCur} dimes')
        if dime < 0:
            dime = 0
        returnCur = 0
        while (price <= -0.05 + epsilon or price <= -0.05 - epsilon) and nickel > 0:
            price += 0.05
            nickel -= 1
            returnCur += 1
        if returnCur > 1 or nickel >= 0:
            if nickel < 0:
                print(f'\t{returnCur - 1} nickels')
            elif returnCur != 0:
                print(f'\t{returnCur} nickels')
        if nickel < 0:
            nickel = 0
            print(f'Machine is out of change.\nSee store manager for remaining refund.\nAmount due is: {(-price)//1:.0f} dollars and {((-price) - (-price)//1)*100:.0f} cents')
            print(price)
            break
        print(f'\nStock contains:\n\t{nickel} nickels\n\t{dime} dimes\n\t{quarter} quarters\n\t{one} ones\n\t{five} fives\n')
        price = input("Enter the purchase price (xx.xx) or `q' to quit: ")

total = nickel*0.05 + dime*0.1 + quarter*0.25 + one + five*5
print(f'\nTotal: {total//1:.0f} dollars and {(total - total//1)*100:.0f} cents')





