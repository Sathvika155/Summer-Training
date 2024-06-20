'''
ip:
7
0 5 3 6 7 2 1
op:
4
'''
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
b=sum(l)
n=(n*(n+1))//2
print(n-b)
    

    
    
    