s=input()
count=1
b=""
for i in range(len(s)-1):
    if(s[i] == s[i+1]):
        count=count+1
    else:
        b=b+s[i]+str(count)
        count=1
b=b+s[i]+str(count)
print(b)
        

        


        
    