n = int(input())

for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end = '')
    print("*" ,end = '')
    for h in range((i-1)*2-1):
        print(" " ,end = '')
    if(i>=2):
        print("*", end = '')
    print("")
