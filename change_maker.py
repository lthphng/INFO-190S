print("Welcome to the vending machine change maker program\nChange maker initialized.")
num_nickels = 25
num_dimes = 25
num_quarters = 25
num_ones = 0
num_fives = 0
stocks = [num_quarters, num_dimes, num_nickels]
change_return_value = [25,10,5]
accepted_choice = ['n', 'd', 'q', 'o', 'f','c','']
accepted_input = ['1','2','3','4','5','6','7','8','9','0','.','-']
print(f'Stock contains:\n   {num_nickels} nickels\n   {num_dimes} dimes\n   {num_quarters} quarters\n   {num_ones} ones\n   {num_fives} fives\n')
input_num = input("Enter the purchase price (xx.xx) or `q' to quit: ")     

while input_num != 'q':
    #exceeding part
    i = 1
    if not input_num:
        print("Invalid purchase price. Try again")
    while i < len(input_num):
        if input_num[i] not in accepted_input or input_num[i]=="-" or input_num.count('.') > 1:
            print('Invalid purchase price. Try again')
            break
        i += 1
    if i == len(input_num):
        if input_num[0] not in accepted_input:
            print("Invalid purchase price. Try again")
        elif input_num == '.':
            print("Invalid purchase price. Try again")
        elif input_num[0]=="-":
            i = 1
            while i <len(input_num):
                if input_num[i] not in accepted_input[:9]:
                    print('Invalid purchase price. Try again')
                    break
                i+=1
            else:
                print("Illegal price: Must be a non-negative multiple of 5 cents.")
        else:
            #normal part
            
            if float(input_num)*100 % 5 != 0 or float(input_num) == 0:
                    print('Illegal price: Must be a non-negative multiple of 5 cents.')
            else:    
                print("Menu for deposits:\n   'n' - deposit a nickel\n   'd' - deposit a dime\n   'q' - deposit a quarter\n   'o' - deposit a one dollar bill\n   'f' - deposit a five dolar bill\n   'c' - cancel the purchase\n")
                 
                
                # calculate the change
                choice = 0
                payment_due = int(float(input_num)*100)
                while payment_due >=0:
                    if int(payment_due) >= 100:
                        print(f'Payment due: {int(payment_due)//100} dollars and {int(payment_due)%100} cents')
                    else:
                        print(f'Payment due: {int(payment_due)} cents')
                    choice = input("Indicate your deposit: ")
                    if choice not in accepted_choice:
                        print(f'Illegal selection: {choice}')
                    else:
                        if choice == 'n':
                            payment_due -= 5
                            num_nickels += 1
                        elif choice == 'd':
                            payment_due -=10
                            num_dimes += 1
                        elif choice =='q':
                            payment_due -=25
                            num_quarters += 1
                        elif choice == 'o':
                            payment_due -=100
                            num_ones += 1
                        elif choice == 'f':
                            payment_due -=500
                            num_fives += 1
                        if payment_due < 0:
                            change = int(abs(payment_due))
                            quarters_change = 0
                            dimes_change = 0
                            nickels_change = 0
                            while num_quarters>0 and change>=25:
                                change -=25
                                quarters_change +=1
                                num_quarters -=1
                            while num_dimes>0 and change>=10:
                                change -=10
                                dimes_change +=1
                                num_dimes -= 1
                            while num_nickels>0 and change>=5:
                                change -=5
                                nickels_change +=1
                                num_nickels -=1
                            print('Please take the change below.')
                            if change == 0:
                                if quarters_change>0:
                                    print(f'   {quarters_change} quarters')
                                if dimes_change>0:
                                    print(f'   {dimes_change} dimes')
                                if nickels_change>0:
                                    print(f'   {nickels_change} nickels') 
                                    
                            elif change > 0 :
                                if quarters_change>0:
                                    print(f'   {quarters_change} quarters')
                                if dimes_change>0:
                                    print(f'   {dimes_change} dimes')
                                if nickels_change>0:
                                    print(f'   {nickels_change} nickels')
                                print('Machine is out of change.\nSee store manager for remaining refund.')
                                if change >= 100:
                                    print(f'Amount due: {(int(abs(payment_due))-quarters_change*25-dimes_change*10-nickels_change*5)//100} dollars and {(int(abs(payment_due))-quarters_change*25-dimes_change*10-nickels_change*5)%100} cents')
                                else:
                                    print(f'Amount due: {(int(abs(payment_due))-quarters_change*25-dimes_change*10-nickels_change*5)%100} cents')
                            print(f'\nStock contains:\n   {num_nickels} nickels\n   {num_dimes} dimes\n   {num_quarters} quarters\n   {num_ones} ones\n   {num_fives} fives\n')
                            break        
                        if payment_due == 0:
                            print('Please take the change below.')
                            print('   No change due.')
                            print(f'Stock contains:\n   {num_nickels} nickels\n   {num_dimes} dimes\n   {num_quarters} quarters\n   {num_ones} ones\n   {num_fives} fives\n')
                            break
                        if choice == 'c':
                            change = int(float(input_num)*100) - payment_due
                            quarters_change = 0
                            dimes_change = 0
                            nickels_change = 0
                            while num_quarters>0 and change>=25:
                                change -=25
                                quarters_change +=1
                                num_quarters -=1
                            while num_dimes>0 and change>=10:
                                change -=10
                                dimes_change +=1
                                num_dimes -= 1
                            while num_nickels>0 and change>=5:
                                change -=5
                                nickels_change +=1
                                num_nickels -=1
                            print('Please take the change below.')
                            if quarters_change>0:
                                print(f'   {quarters_change} quarters')
                            if dimes_change>0:
                                print(f'   {dimes_change} dimes')
                            if nickels_change>0:
                                print(f'   {nickels_change} nickels')
                                
                            if change > 0 :
                                print('Machine is out of change.\nSee store manager for remaining refund.')
                                if change >= 100:
                                    print(f'Amount due: {(int(float(input_num)*100) - payment_due-((quarters_change*25)+(dimes_change*10)+(nickels_change*5)))//100} dollars and {(int(float(input_num)*100) - payment_due-(quarters_change*25+dimes_change*10+nickels_change*5))%100} cents')
                                else:
                                    print(f'Amount due: {(int(float(input_num)*100) - payment_due-(quarters_change*25+dimes_change*10+nickels_change*5))%100} cents')
                            print(f'\nStock contains:\n   {num_nickels} nickels\n   {num_dimes} dimes\n   {num_quarters} quarters\n   {num_ones} ones\n   {num_fives} fives\n')
                            break
    
    input_num = input("Enter the purchase price (xx.xx) or `q' to quit: ")            
else: 
    print(f"Total: {(num_nickels*5 + num_dimes*10 + num_quarters*25 + num_ones*100 + num_fives*500)//100} dollars and {(num_nickels*5 + num_dimes*10 + num_quarters*25 + num_ones*100 + num_fives*500)-(100*(num_nickels*5 + num_dimes*10 + num_quarters*25 + num_ones*100 + num_fives*500)//100)} cents")
