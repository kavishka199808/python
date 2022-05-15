def sum(num):
    if num == 1:
        return 1

    return sum(num-1)+ num


while True:
    n = int(input("Enter number for n: "))
    if n == -1:
          break

    print(sum(n))
