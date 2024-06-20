a=input()
b=input()
c=''
d=''
for i in a:
    if (i.isdigit()):
        c=c+i
for i in b:
    if(i.isdigit()):
        c=c+i
print(c)
for i in c:
    if i not in d:
        d=d+i
d=list(d)
d.sort(reverse = True)
if (int(d[-1])%2==0):
    print(''.join(d))
else:
    min=0
    for i in range(len(d)-2,-1,-1):
        if(int(d[i]%2)==0):
            d.append(d.pop(i))
            print(''.join(d))
        

    
