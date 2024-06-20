'''
ip:[3,5,9,6,8,10]
'''
a=[3,5,9,6,8,10]
print(a)
min=0
l=[]
for i in range(len(a)):
    if a[i]>min:
        min=a[i]
        l.append(a[i])
    else:
        l.append(min)
max=0
r=[]
n=len(a)
for i in range(len(a)-1,-1,-1):                           
    if a[i]>max:
        max=a[i]
        r.append(a[i])
    else:
        r.append(max)
p=[]
q=[]
for i in range(len(a)):
    if l[i]<=a[i]:
        p.append(a[i])
    if r[i]<=a[i]:
        q.append(a[i])
print(p)
print(q)
    
  