'''
ip:
school
3
L 2->hoolsc
R 3->oolsch
L 1->chools
op:
yes
hoc
sch,cho,hoo,ool
'''
str=input()
q=int(input())
a=[]
x=''
for i in range(q):
    a.append(input())
    a.append(int(input()))
for j in range(0,len(a),2):
    if(a[j]=='L'):
        x=x+str[a[j+1]]
    elif(a[j]=='R'):
        x=x+str[a[-(j+1)]]
x=list(x)
x.sort()
print(x)
a1=[]
for i in range(len(str)-(q-1)):
    t=list(str[i:q+i])
    t.sort()
    a1.append(t)
print(a1)
for i in a1:
    if(i==x):
        print('yes')
        break
else:
    print('no')
        
    
    



        

             
    
    
