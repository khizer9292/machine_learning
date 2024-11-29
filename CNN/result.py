print('Enter the number and I will give you the table of that number')

ans = 'y'

def table(n):
    print('The table of', n, 'is')
    if n < 0:
        print('please Enter the positive number')
    elif n == 0:
        print('Please Enter the postive number other than zero')
    else:
        for i in range(1,11):
            print(f"{n} x {i} = " ,  n * i, end='\n' )
        
        


while ans == 'y':
    n = int(input('Enter the number:'))
    table(n)
    print('Thanks for using this program, Can you want to try this on another number?? (y/n)')
    ans = str(input('')).lower()
    if ans != 'y':
        print("Exiting the program, Good Bye!!")
        break
        

     
