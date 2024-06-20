i=input()
l=i.split(',')
s=''
for i in l:
    b=i.split(':')
    print(b)
    if(str(len(b[0])) in b[1]):
        s=s+b[0][-1]
    else:
        for i in range(len(b[0])-1,0,-1):
            if(str(i)) in b[1]:
                s=s+b[0][i-1]
                break
        else:
            s=s+'x'
print(s)