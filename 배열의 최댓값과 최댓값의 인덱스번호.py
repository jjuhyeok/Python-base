s =[8, 6, 9, 10, 4, 7, 10, 6, 8, 7]
Max = 0
c = 0
k = 0
Max = s[0]
for i in range(len(s)):
    c = c+1
    if Max<s[i]:
        Max = s[i]
        k = c - 1
print("s =",s)
print("Max = ",Max)
print("Idx = ",k)
