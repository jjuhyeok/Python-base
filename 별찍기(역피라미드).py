n = int(input()) #홀수만

for i in range(n,0,-2):
    for k in range(int(-((i-n)/2))):
        print(" ",end = '')
    for j in range(i):
        print("*",end = '')
    print("")
