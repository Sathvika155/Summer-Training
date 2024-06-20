l=[4,9,8,2,14,33,15,6]
t=[]
for i in range(len(l)-2):
        j=i+2
        p=l.index(min(l[i:j+1]))
        t=l[p]
        l[p]=l[i]
        l[i]=t
        j=j+1
print(l)
        
                    
            

       

        