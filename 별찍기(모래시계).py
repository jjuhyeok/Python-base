n = int(input())

for i in range(2*n-1,0,-2):
    for k in range(int((2*n-i)//2)):
        print(" ", end = '')
    for j in range(i):
        print("*", end = '')
    print("")

for i in range(3,2*n,2):
    for k in range(int((2*n-i)//2)):
        print(" ", end = '')
    for j in range(i):
        print("*", end = '')
    print("")
