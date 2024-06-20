def add(n):
    p=0
    r=0
    while(n>0):
        r=n%10
        p=p+r
        n=n//2
    return p
def prime(x):
    if x in [2,3,5,7]:
        return m
    else:
        return m+1
        
n=int(input())
m=n
if(n<10):
    print(prime(n))
else:
    while(1):
        n=add(n)
        if(n<10):
            break
    print(prime(n))
        

