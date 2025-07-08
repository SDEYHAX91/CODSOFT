class Calc:     ## CLASS

    ## ALL OPERATION METHODS
    def add(self, x, y):     ## ADDITION           

        if (x + y) == int(x + y):
            print(f"{x} + {y} = {int(x + y)}")
        else:
            print(f"{x} + {y} = {round((x + y), 4)}")


    def sub(self, x, y):    ## SUBTRACTION

        if (x - y) == int(x - y):
            print(f"{x} - {y} = {int(x - y)}")
        else:
            print(f"{x} - {y} = {round((x - y), 4)}")


    def product(self, x, y):        ## PRODUCT

        if (x * y) == int(x * y):
            print(f"{x} * {y} = {int(x * y)}")
        else:
            print(f"{x} * {y} = {round((x * y), 4)}")


    def div(self, x, y):            ## DIVISION

        if x % y == 0:
            print(f"{x} / {y} = {int(x / y)}")
        else:
            print(f"{x} / {y} = {round((x / y), 4)}")

    
obj = Calc()        ## OBJECT

x = float(input("Enter 1st number: "))      ## INPUT NUMBERS
y = float(input("Enter 2nd number: "))

if x == int(x):     
    x = int(x)
if y == int(y):
    y = int(y)

## OPERATIONS MENU
print('''           
Operations:
          
1. Addition (+)
2. Subtraction (-)
3. Product (*)
4. Division (/)
''')    
    
choice = int(input("Enter operation(1-4) : "))      ## INPUT CHOICE

match choice:                                       ## OPERATIONS

        case 1:     obj.add(x, y)

        case 2:     obj.sub(x, y)

        case 3:     obj.product(x, y)

        case 4:     obj.div(x, y)

        case __:    print("Invalid! Try again next time.")
    