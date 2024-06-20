str=input()
l=[]
for i in str:
    if(i!='*'):
        l.append(i)
    else:
        l.pop()
print(''.join(l))
        
        