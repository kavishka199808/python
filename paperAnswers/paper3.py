#power fuction implementation

def power(base,exp):
    if(exp == 0):
        return 1
    return base * power(base,exp-1)

#read integers from keyboard input
#x = base
#n = exp

while True:
    x=int(input("Enter number1 : "))
    n=int(input("Enter number2 : "))

    if x==-1 or n==-1:
        break

    print(power(x,n))
