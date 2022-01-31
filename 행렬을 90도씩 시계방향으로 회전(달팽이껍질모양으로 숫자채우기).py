n = int(input())
N = n
x = [[0 for j in range(n)] for i in range(n)] 
a = 0 
b = -1 
c = 1 
d = 1 
print("#0")
while n > 0: 
    for i in range(n): 
        b += d
        x[a][b] = c
        c += 1
    n -= 1 
    for j in range(n): 
        a += d
        x[a][b] = c
        c += 1
    d *= -1
for i in x:
    for j in i:
        print('%03d' %j , end=' ')
    print()

print("#90")
c = 1
a = -1 
b = N-1
d = 1
n = N
while n > 0: 
    for i in range(n): 
        a += d
        x[a][b] = c
        c += 1
    n -= 1 
    for j in range(n): 
        b -= d
        x[a][b] = c
        c += 1
    d *= -1
for i in x:
    for j in i:
        print('%03d' %j , end=' ')
    print()

print("#180")


c = 1
a = N-1 
b = N
d = 1
n = N
while n > 0: 
    for i in range(n): 
        b -= d
        x[a][b] = c
        c += 1
    n -= 1 
    for j in range(n): 
        a -= d
        x[a][b] = c
        c += 1
    d *= -1
for i in x:
    for j in i:
        print('%03d' %j , end=' ')
    print()

print("#270")
c = 1
a = N 
b = 0 
d = 1
n = N
while n > 0: 
    for i in range(n): 
        a -= d
        x[a][b] = c
        c += 1
    n -= 1 
    for j in range(n): 
        b += d
        x[a][b] = c
        c += 1
    d *= -1
for i in x:
    for j in i:
        print('%03d' %j , end=' ')
    print()


print("#360")
a = 0 
b = -1 
c = 1 
d = 1 
n = N
while n > 0: 
    for i in range(n): 
        b += d
        x[a][b] = c
        c += 1
    n -= 1 
    for j in range(n): 
        a += d
        x[a][b] = c
        c += 1
    d *= -1
for i in x:
    for j in i:
        print('%03d' %j , end=' ')
    print()
