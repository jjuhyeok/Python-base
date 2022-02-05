user_info={'name':'David','age':'21','address':'Gwangjin-gu,Seoul'}

N=int(input()) #변경할 횟수

for i in range(N):
    print("Edit #",i+1)
    a=input()
    b=input()
    user_info[a]=b
    
print("USER INFO")
for i in user_info:
    print(i,":",user_info[i])
