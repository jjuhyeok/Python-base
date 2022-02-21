n = int(input())10
a = 1
b = 0
for k in range(n*2-1):
    for i in range(a):
        print("*", end = '')
    print("")
    if(a == n):
        b = 1
    if(b == 1):
        a = a - 1
    else :
        a = a + 1
    if(a == 0):
        break
