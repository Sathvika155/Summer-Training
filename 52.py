a=[2,5,2,3,6,7,1,0,5,7]
print(a)
min=0
l=[]
for i in range(len(a)):
    if a[i]>min:
        min=a[i]
        l.append(a[i])
    else:
        l.append(min)
print(l)
max=0
r=[]
n=len(a)
for i in range(len(a)-1,-1,-1):                           
    if a[i]>max:
        max=a[i]
        r.append(a[i])
    else:
        r.append(max)
print(r)
sum=0
for i in range(len(a)):
    if l[i]<r[i]:
        sum=sum+(l[i]-a[i])
    else:
        if l[i]==r[i]:
            sum=sum+(l[i]-a[i])
print(sum)
    
        

