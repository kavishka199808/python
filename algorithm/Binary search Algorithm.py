#impelementation
#A = array
#low = Start_Index
#high = End_Index
#x = search value

arr = []
for v in range(5):
    arr.append(int(input('Enter number :')))
print(arr)

x = int(input('Enter the search value : '))

def binary_Search(arr,low,high,x):
        #check base case
    if high >=low:

        mid=(high+low)//2

        if arr[mid] == x :
            return mid
        elif arr[mid] > x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid + 1,high,x)
    else:
        return -1

#Function call
result = binary_Search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index",str(result))
else:
    print("Element is not present in array")
        
