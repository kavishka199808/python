A= []
for v in range(10):
    A.append(input('Enter a number'))
print(A)

def insertionsort(A):
    for j in range(1,len(A)):
         key = A[j]
         i = j-1
         while (i>0 and A[i]>key):
             A[i+1] =A[i]
             i=i-1
         A[i+1] = key

insertionsort(A)
print('sorted Array')
for a in range(len(A)):
    print(A[a])

