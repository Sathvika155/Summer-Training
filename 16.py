str=input()
count=0
count2=0
for i in range(len(str)):
    count+=str[i]=='M'
    count2+=str[i]=='F'
if(count>count2):
    print("M")
else:
    print("F")

