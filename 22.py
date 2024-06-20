'''
ip:
3->3*3 matrix
xyz
pqr
abc
"yraxpznqs"
op:
yes
'''
n=int(input())
index=0
matrix = []
count=0
s=[]
for i in range(n):          
    matrix.append(input())
str=input()   
for i in range(len(str)):
    if str[i] in matrix[index%n]:
        matrix.replace(matrix[index],"*")
        continue
    else:
        flag=1
        print("no")
if(flag==0):
    print('yes')
        
       



