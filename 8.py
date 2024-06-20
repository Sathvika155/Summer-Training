'''
ip:
  13
op:
   13
ip:
  14
op:
   17'''
'''
n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if(count==2):
    print(n)
else:
    n=n+1
 '''   
def prime(n):
    count=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            count=count+1
    if(count==0):
        return True
    else:
        return False
n=int(input())
while(n):
    if(prime(n)):
        print(n)
        break
    else:
        n=n+1

