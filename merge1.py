a=[1,5,8,9]
b=[2,7,9,10,14]
c=[]
i,j=0,0
while(i<len(a) and j<len(b)):
    if(a[i]<b[j]):
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j]) 
        j=j+1
if(j<len(b)):
    c.extend(b[j:])
if(i<len(a)):
    c.extend(a[i:])
print(c)