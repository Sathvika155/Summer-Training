'''
ip:[0,0,1,1,1,2,2,3,4]
op:[0,1,2,3,4]'''

list=input().split()
l=[]
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if(list[i]==list[j]):
            if(list[i] not in l):
                l.append(nums[i])
            else:
                l.append(nums[j])
print(l)
            
                   
    
               





'''
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i] == nums[j]):
                    if(nums[i] not in l):
                        l.append(nums[i])
                else:
                    l.append(nums[j])
        return l'''