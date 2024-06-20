str=input()
s=''
count=0
for i in str:
    if i not in s:
        s=s+i
a='abcdefghijklmnopqrstuvwxyz'
for i in s:
    if i in a:
        count=count+1
if(count==26):
    print('yes')
else:
    print('no')