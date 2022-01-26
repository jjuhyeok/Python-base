n = int(input())
for i in range(n):
    a = input()
    l = list(a.split())
    p = int(l[0]) + int(l[1]) + int(l[2])
    p = p /3
    p = round(p,2)
    print("Student %d's Average Score :"%(i+1),p)
    
