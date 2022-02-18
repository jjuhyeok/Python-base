n = int(input())

for i in range(1,n*2+1):
    if(i>n):
        for j in range(2*n-i):
            print("*",end = '')
    else:
        for j in range(i):
            print("*",end = '')
    if(i>n):
        for k in range(i*2-2*n):
            print(" ", end = '')
    else:
        for k in range(2*n-i*2):
            print(" ", end = '')
    if(i>n):
        for h in range(2*n-i):
            print("*", end = '')
    else:
        for h in range(i):
            print("*", end = '')
    print(" ")
        
