'''
ip:7

1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch
4 school
'''

n=int(input())
l=[]
count=0
for i in range(n):
    a=int(input())
    b=input()
    if a==1:
        if b not in l:
            l.append(b)
    if a==2:
        for i in l:
            if i==b:
                print("True")
                break
        else:
            print("False")
    if a==3:
        for i in l:
            if i.startswith(b):
                count=count+1
        print(count)
    if a==4:
        if b in l:
            l.remove(b)
        print(l)
            
        
    
    