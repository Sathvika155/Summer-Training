'''
ip:xyzabcdefklmnopqefgh"
op:7'''
str=input()
count=1
max=0
for i in range(len(str)-1):
    if ord(str[i]) == (ord(str[i+1]))-1:
        count=count+1
    else:
        if(count>max):
            max=count
        count=1
if(count>max):
    max=count
print(max)
                   