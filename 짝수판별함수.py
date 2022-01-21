def countEvenNums(n):
    cnt=0
    for i in range(2,n+1,2):
        cnt+=1
    return cnt

n = int(input())
print("The number of evens is", countEvenNums(n))
