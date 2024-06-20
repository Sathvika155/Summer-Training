'''ip:
300
400
op:count of numbers divisble by 7 from 300 to 400'''
count=0
for i in range(300,401):
    if(i%7 == 0):
        count=count+1
    
print(count)