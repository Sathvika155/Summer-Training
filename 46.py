'''
[5,3,2,9,4]
[8,9,5,3,6,9]
'''
def check(l1,l2,i,j,l3):
    if i==len(l1):
        return l3
    else:
        if l1[i]%2==0:
            if j==len(l2):
                return
            else:
                if(l2[j]!=0):
                    l3.append(l1[i]+l2[j])
                return check(l1,l2,i,j+1,l3)
        else:
            return check(l1,l2,i+1,j,l3)  
l1=[6,3,2,9,4]
l2=[8,9,5,3,6,9]
l3=[]
i=0
j=0
a=check(l1,l2,i,j,l3)
print(a)
'''while(l1):
    if(l1[i]%2==0):
        while(l2):
            if(l2[j]%2!=1):
                l3.append(l1[i]+l2[j])
            else:
                l2[i]=l2[i+1]
    else:
        l1[i]=l1[i+1]
print(l3)'''

