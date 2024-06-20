n=int(input())
pos=int(input())
l=[]
max=0
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
print(l[-pos])
        
            
        
        
    
