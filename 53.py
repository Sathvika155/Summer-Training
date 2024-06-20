def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in m:
        for j in range(1,n+1):
            if(j>=i):
                if l1[j-i]!=-1:
                    if(l1[j]!=-1):
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
    
               

m=[3,4,5]
n=10
fun()



        
