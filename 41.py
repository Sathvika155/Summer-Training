'''
def check(r,c):
    if r<0 or c<0 or r>=len(m) or c>=len(m) or m[r][c]!=1:
        return
    else:
        if m[r][c]==1:
            m[r][c]=2
        check(r-1,c)
        check(r,c-1)
        check(r+1,c)
        check(r,c+1)
n=int(input())
r=int(input())
c=int(input())
m=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    m.append(a)
check(r-1,c-1)
count=0
for i in range(len(m)):
    for j in range(len(m)):
        if m[r][c]==1:
            count=count+1
print(count)
'''
def check(i,j):
    
    if i<0 or i>len(l)-1 or j<0 or j >len(l)-1:
        return
    if l[i][j]==0:
        return 
    else:
        #print('d')
        if l[i][j]==1:
            l[i][j]=0
        #print(l)
        check(i-1,j)
        check(i,j-1)
        check(i+1,j)
        check(i,j+1)
    return 
        
n=int(input())  
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    l.append(a)
r=int(input())
c=int(input())
check(r-1,c-1)
c=0
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][j]==1:
            c=c+1
print(l)
print(c)


                                                    
                                                                          