def fac(x):
    if x==0:
        return 0 
    return x+fac(x-2)
n=13
if(n%2==0):
    print(fac(n))
else:
    print(fac(n-1))
