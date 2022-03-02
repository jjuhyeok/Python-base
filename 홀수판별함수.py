def countoddNums(n):
    cnt=0
    for i in range(1,n+1,2):
        cnt+=1
    return cnt

n = int(input())
print("The number of odd is", countoddNums(n))
