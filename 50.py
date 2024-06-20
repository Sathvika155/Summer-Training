n=7262
a=0
b=0
c=0
while(n):
    if(n>=3600):
        a=int(n/3600)
        print(a,end="h:")
    n=n-(a*3600)
    if(n>=60):
        b=int(n/60)
        print(b,end="m:")
    n=n-(b*60)
    if(n<60):
        print(n,end="s")
        break

        
        