a = int(input())

if a<=1:
    print("Inavailable Number")
elif a%2 != 0:
    a = a
    for i in range (1,a+1):
        print("\n")
        if i == 1 or i == a or i == (a+1)/2:
            for j in range(1,a+1):
                print("*",end="")
        else :
            for j in range(1,a+1):
                if j == 1 or j == a or j == (a+1)/2:
                    print("*",end="")
                else :
                    print(" ",end="")
else :
    a = a*2+1
    for i in range (1,a+1):
        print("\n")
        if i == 1 or i == a or i == (a+1)/2:
            for j in range(1,a+1):
                print("*",end="")
        else :
            for j in range(1,a+1):
                if j == 1 or j == a or j == (a+1)/2:
                    print("*",end="")
                else :
                    print(" ",end="")

