n = int(input("Enter the total number of 1's and 0's: "))

for i in range(n):
    if i%2==0:
        print('1', end=' ')
    else:
        print('0', end=' ')