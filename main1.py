n = int(input())
a = 1
b = 1
for i in range(0,n):
    if i ==0:
         print(" "*(n-1), end="")
    while a != i+1:
        if b == 1:
            print(" "*(n-i-1), end="")
            b =0
        print(a,end ="")
        a=a+1
    while a != 0:
        print(a,end="")
        a=a-1
    print('')
    a = 1
    b = 1
    
