def queen(r):
    if r==n:
        return
    for c in range(n):
        if check(r,c):
            m[r][c]='q'
            break
    return queen(r+1)

def check(i,j):
    if i==a:
        return 0
    elif j==b:
        return 0
    r=i
    c=j
    for i in range(j+1):
        if m[i][j]=='q':
            return 0
    i=r
    while(i>=0 and j>=0):
        if m[i][j]=='q':
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):
        if m[i][j]=='q':
            return 0
        r=r-1
        c=c+1
    return 1
n=int(input())
a=int(input())#rook position
b=int(input())
m=[]
for i in range(n):
    m.append([0]*n)
m[0][0]=1
queen(0)
print(m)