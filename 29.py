'''
l=[4,8,2,4,1,4,8,4]
n=len(l)
for i in l:
    c=l.count(i)
    if(c>n//2):
        f=c
print(c)
'''
l=[4,2,4,4,4,8,8]
n=len(l)
w=0
count=1
for i in range(len(l)):
    if(l[i]==l[i-1]):
        count=count+1
    else:
        count=count-1
        if(count==0):
            count=count+1
            w=l[i]
print(w)

    
    