a=int(input())
b=int(input())
for i in range(2,min(a,b)//2):
    if(a%i==0) and (b%i==0):
        print('ncp')
        break
    else:
        print('cp')


            
