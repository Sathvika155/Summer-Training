str=input()
s=str.split()
l=[0]*len(s)
for i in s:
    l[int(i[-1]-1)]=i[:-1]
print(''.join(l))
    
        
        
        
    