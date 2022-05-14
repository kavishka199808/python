B = []
for v in range(6):
    B.append(int(input('Enter a Number :')))
print(B)

#implementation of selectionSort
def selectionSort(B):
    n = len(B)
    for j in range (0,n-1):
        smallest = j
        for i in range (j+1,n):
            if B[i] < B[smallest]:
                smallest = i
        B[j],B[smallest] = B[smallest],B[j]

#call the selectionSort
selectionSort(B)
print("Sorted Array :")
print(B)
        
