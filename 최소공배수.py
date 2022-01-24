def get_gcd(n1,n2):
    if(n1<n2):
        a=n1
    else:
        a=n2
    for i in range(1,a+1):
        if(n1%i==0 and n2%i==0):
            gcd=i
    a = n1/gcd
    b = n2/gcd
    c = gcd*a*b
    return c

n1=int(input())
n2=int(input())
print(get_gcd(n1,n2))
