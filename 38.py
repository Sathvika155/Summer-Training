'''
ip:
    [3,2,4,1,3,6,7,2]
    
op:
    3 2 4 1
    3 6 7 2
    '''
'''def list(l):
    i=0
    newlist=[]
    newlist1=[]
    for i in l:
        if i not in newlist:
            newlist.append(i)
        else:
            newlist1.append(i)
            
    return newlist
    '''
l=[1,2,3,4,1,2,3,1,2]
m=[]
count=0
while(count!=len(l)): 
    l1=[]
    for i in range(len(l)):
        if (not str(l[i]).isalpha()):
            if l[i] not in l1:
                count=count+1
                l1.append(l[i])
                l[i]='a'
    m.append(l1)
print(m)
            
    
