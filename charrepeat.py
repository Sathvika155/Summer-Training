s="f46feLK9y56u#@&56hIjbn6KJhA"
lc,lv,uc,uv,d,s=0,0,0,0,0,0
for i in s:
    if(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isupper()):
        if(i in 'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
    elif(i.isdigit()):
        d=d+1
    elif(i.isalnum()):
        s=s+1
print(lv)
    
        
