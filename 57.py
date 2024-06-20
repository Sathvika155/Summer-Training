s=input()
a=''
for i in s:
    if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
        pass
    else:
        a=a+i
a=list(a)
a.sort(reverse = True)
s=''.join(a)
print(s)
    