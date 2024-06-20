a=int(input())
for i in range(2,(a//2)+1):
    if(isprime(i) and isprime(a-i)):
        print('yes')
        break
else:
    print('no')
    
def isprime(a):
    if(a==1):
        return 1
    if(a==2):
        return 1
    for i in range(2,(a//2+1)):
        if(x%i==0):
            return 1
    return 0
        