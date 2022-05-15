#Fibonacci function implementation

def Fibonacci(num):
    if num <= 1 :
        return num
    
    return Fibonacci(num - 1) + Fibonacci(num - 2)

#read an integer from keyboard
#n=input number
#num = paramiter name

while True:
    n = int(input("Enter number : "))
    if n == -1:
        break
    print(Fibonacci(n))

