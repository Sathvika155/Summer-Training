s=input()
b=list(s)
a=''
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        a=a+i
a=list(a[::-1])
for i in range(len(b)):
    if ord(b[i])>=97 and ord(b[i])<=122:
        pass    
    else:
        a.insert(i,b[i])        
s = ''.join(a)
print(s)

        
        