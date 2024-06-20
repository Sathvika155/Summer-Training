'''
l=[3,2,5,4,1,6,8]
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            print(l[i],l[j],l[k],end=",")
            print()           
'''
def combination(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=[3,2,5,4,1,6,8]
k=3
combination(a,k)
    


'''
l=[3,2,5,4,1,6,8]
print(pairs(l,0,1,2))

'''
    
        

