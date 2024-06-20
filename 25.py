'''
ip:5 3 7 8 4
'''



'''
l=[9,8,7,6,5,4]
min=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        profit=l[i]-l[j]
        if(profit<min):
            min=profit
print(abs(min))

'''
l=[15,3,2,7,8,4]
min=0
for i in range(len(l)-1):
    profit=l[i]-l[i+1]
    if(profit<min):
        min=profit
print(abs(min))

        
        
        