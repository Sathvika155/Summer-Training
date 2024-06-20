'''
ip:khoor
3
op:
hello
str=input()
key=int(input())
s=''
a=0
for i in str:
    if(ord(i)-key<97):
        a=97-(ord(i)-key)
        a=(122-(a-1))
        s = s +chr(a)
    else:
        s = s +chr(ord(i)-key)
print(s)

char((ord(i)-key)-97)%26+97))
'''
str=input()
key=int(input())
a=key%26
s=''
for i in str:
    if(ord(i)-a>=97):
        s=s+chr(ord(i)-97)
    else:
        s=s+chr(ord(i)-a+26)
print(s)
