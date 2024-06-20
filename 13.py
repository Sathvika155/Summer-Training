'''a=[2,3,4,5]
b=[6,7,8,9]
op:(12,17)
'''
def add(x,even):
    t=0
    if(x == len(a)):
        return even
    if(a[x]%2==0):
        even=even+a[x]
    t=add(x+1,even)
    return t

def add2(x,odd):
    t=0
    if(x==len(b)):
        return odd
    if(b[x]%2==1):
        odd=odd+b[x]
    t=add2(x+1,odd)
    return t
a=[2,3,4,5]
b=[6,7,8,9]
even=0
odd=0
print(add(0,0))
print(add2(0,0))
