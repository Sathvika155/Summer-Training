'''def dfs(d,l,x):
    l.append(x)
    for i in d[x]:
        if i not in l:
            dfs(d,l,i)

def possiblepath(d,x):
    l.append(x)
    if (x==2):
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in l:
            possiblepath(d,i)
    l.pop()

def cost(d,x,e,s):
    l.append(x)
    if (x==e):
        print(l,'-',s)
        l.pop()
        return s
    for i in d[x]:
        if i[0] not in l:
            cost(d,i[0],e,s+i[1])
    l.pop()
    
def min_cost(d,x,e,c,m):
    l.append(x)
    if(x==e):
        if(c<m):
            m=c
            return m
        l.pop()
        return m
    for i in d[x]:
        if i[0] not in l:
            m=min_cost(d,i[0],e,c+i[1],m)
    l.pop()
    return m

def shortest_costpath(d,x,e,c,m,l1):
    l.append(x)
    if(x==e):
        if(c<m):
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]:
        if i[0] not in l:
            m,l1=shortest_costpath(d,i[0],e,c+i[1],m,l1)
    l.pop()
    return m,l1
'''
def bfs(d,x):
    v=[]
    q=[x]
    while(q):
        x=q[0]
        for i in d[x]:
            if i not in v and i not in q:
                q.append(i)
        v.append(q.pop(0))
        print(v[-1])
        
def dijkstra(dict,x):
    d={5:9999,7:9999,4:9999,8:9999,3:9999,2:9999}
    d[x]=0
    v=[]
    q=[x]
    min=0
    while(q):
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                x=i      
        for i in dict[x]:
            if(i[0] not in v):
                q.append[i[0]] 
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
        v.append(x)
        q.remove(x)
    return d
   
dict={5:[(7,1),(3,2)],7:[(5,1),(4,3),(3,1)],4:[(7,3),(8,2),(2,3)],8:[(3,4),(4,2),(2,5)],3:[(5,2),(7,1),(8,4)],2:[(4,3),(8,5)]}
'''l=[]
dfs(dict,l,5)'''
'''possiblepath(dict,5)'''
'''cost(dict,5,2,0)'''
'''min_cost(dict,5,2,0,999999)
print(a)
#print(l)'''
''''a=shortest_costpath(dict,5,2,0,9999999,[])
print(a)'''

dijkstra(dict,5)

