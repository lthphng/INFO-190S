nickel = 25
dime = 25
quarter = 25
one = 0
five = 0

illegal = 0

print('Welcome to the vending machine change maker program\n'
      'Change maker initialized.')
print('Stock contains:')
print(f'   {nickel} nickels') #5 cents
print(f'   {dime} dimes') #10 cents
print(f'   {quarter} quarters') #25 cents
print(f'   {one} ones') #1 dollar = 100 cents
print(f'   {five} fives') #5 dollars = 500 cents


valid = input("\nEnter the purchase price (xx.xx) or `q' to quit: \n")

while valid!='q':
      valid=float(valid)

      if valid*100%5==0:
            print('\nMenu for deposits:\n'
                  "\t'n' - deposit a nickel\n"
                  "\t'd' - deposit a dime\n"
                  "\t'q' - deposit a quarter\n"
                  "\t'o' - deposit a one dollar bill\n"
                  "\t'f' - deposit a five dollars bill\n"
                  "\t'c' - cancel the purchase\n"
                  )

            while valid>1:
                  print(f"Payment due: {(valid)//1:.0f} dollars and {((valid)-(valid)//1)*100:.0f} cents")
                  select = input("Indicate your deposit: \n")

                  if select != 'n' and select != 'd' and select != 'q' and select != 'o' and select != 'f' and select != 'c':
                        illegal+=1
                        print(f"Illegal selection: {illegal}")
                  elif select=='c':
                        break
                  else:
                        if select=='n':
                              valid-=0.05
                              nickel+=1
                        elif select=='d':
                              valid-=0.1
                              dime+=1
                        elif select=='q':
                              valid-=0.25
                              quarter+=1
                        elif select=='o':
                              valid-=1
                              one+=1
                        elif select=='f':
                              valid-=5
                              five+=1

            while 0<valid<1:
                  print(f"Payment due: {valid*100:.0f} cents")
                  select=input("Indicate your deposit: ")
                  if select != 'n' and select != 'd' and select != 'q' and select != 'o' and select != 'f' and select != 'c':
                        illegal+=1
                        print(f"Illegal selection: {illegal}")
                  elif select=='c':
                        break
                  else:
                        if select == 'n':
                              valid -= 0.05
                              nickel += 1
                        elif select == 'd':
                              valid -= 0.1
                              dime += 1
                        elif select == 'q':
                              valid -= 0.25
                              quarter += 1
                        elif select == 'o':
                              valid -= 1
                              one += 1
                        elif select == 'f':
                              valid -= 5
                              five += 1

            if valid<0 or select=='c':
                  print("\nPlease take the change below.")
                  if quarter>0 and (-valid>=0.25 or valid>0.25):
                        if valid<0:
                              print(f"\t{-valid//0.25:.0f} quarters")
                              quarter -= -valid // 0.25
                        else:
                              print(f"\t{valid//0.25:.0f} quarters")
                              quarter -= valid // 0.25
                        valid%=25
                  if dime>0 and (-valid>=0.1 or valid>0.1):
                        if valid<0:
                              print(f"\t{-valid//0.10:.0f} dimes")
                              dime -= -valid // 0.1
                        else:
                              print(f"\t{valid // 0.10:.0f} dimes")
                              dime -= valid // 0.1
                        valid%=10

                  if nickel>0 and (-valid>0 or valid>0):
                        if valid<0:
                              print(f"\t{-valid//0.05:.0f} nickels")
                              nickel -= -valid // 0.05
                        else:
                              print(f"\t{valid//0.05:.0f} nickels")
                              nickel -= valid // 0.05

            print('\nStock contains:\n'
                  f'\t{nickel:.0f} nickels\n'  # 5 cents
                  f'\t{dime:.0f} dimes\n'  # 10 cents
                  f'\t{quarter:.0f} quarters\n'  # 25 cents
                  f'\t{one:.0f} ones\n'  # 1 dollar = 100 cents
                  f'\t{five:.0f} fives'  # 5 dollars = 500 cents
                  )

      else:
            print('\nIllegal price: Must be a non-negative multiple of 5 cents.')
      valid = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")

if valid=='q':
      total = nickel*0.05 + dime*0.1 + quarter*0.25 + one*1 + five*5
      print(f"\nTotal: {(total)//1:.0f} dollars and {((total)-(total)//1)*100:.0f} cents")
