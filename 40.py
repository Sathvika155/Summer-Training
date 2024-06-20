str=input()
max=0
d={}
i=0
s=''
while(i<len(str)):
      while(i<len(str)):
        if str[i] not in s:
            s=s+str[i]
            d[s[i]]=i
        else:
            if(len(s)>max):
                max=len(s)
            s=''
            break
        i=i+1
        i=d[str[i]]+1
print(max)
        
    
            
        
