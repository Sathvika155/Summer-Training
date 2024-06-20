a=[3,4,5,7,2,3,4,8,6,9]
b=[]
for i in a:
    if(i not in b):
        b.append(i)
for i in b:
    print(i,"-",a.count(i))
    