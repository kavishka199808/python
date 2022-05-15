def sumcube(num):
    if num == 1:
        return 1
    
    return sumcube(num - 1)+ num * num * num

while True:
     n = int(input("Enter numbers : "))
     if n == -1:
         break
        
     print(sumcube(n))
