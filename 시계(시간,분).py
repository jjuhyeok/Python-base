n1=int(input())
n2=int(input())

for i in range(n1+1):
    if(i>23):
            break
    for j in range(60):
        if(i==n1 and j==n2+1):
            break
        print("%.02d : %.02d"%(i,j))
