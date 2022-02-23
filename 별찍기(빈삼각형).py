n = int(input())

for i in range(1,n+1):
    if(i == n):
        for h in range(n*2-1):
            print("*",end = '')
    elif(i == 1):
        for j in range(n-1):
            print(" ", end = '')
        print("*")
    else:      
        for j in range(n-i):
            print(" ", end = '')
        print("*",end = '')
        for k in range((i-1)*2-1):
            print(" ",end = '')
        print("*")
