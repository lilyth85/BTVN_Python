n=int(input("nhập vào chiều dài tam giác: "))
m=2*n
for i in range (1,m):
    if i<n:
        print ('  '*(n-i), '* '*i)
    elif i==n:
        print ((i*2)*' *')
    elif n < i <=m:
        print (m*' ', ((m-i)*'* '))