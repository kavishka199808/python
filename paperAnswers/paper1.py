def multiply(num1,num2):
    
    if num2 == 1 :
        return num1
   
    return (num1 + multiply(num1,num2-1))

while True:
        M = int(input("Enter number m : " ))
        n = int(input("Enter number n : "))

        if M == -1 or n == -1:
              break
        print(multiply(M,n))
    
