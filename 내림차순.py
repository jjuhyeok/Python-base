s=[]
for i in range(5):
    a=int(input())
    s.append(a)
print("before = ",s)

s.sort(reverse = True)
print("after = ",s)
