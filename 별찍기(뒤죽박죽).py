n = int(input())

for i in range(1,n+1):
    if(n % 2 == 0):
        a = n-1
    else:
        a = n
    for j in range(int(a/2)+1):
        print("* ",end = '')
    print("")
    for k in range(int(n/2)):
        print(" *",end = '')
    print("")
