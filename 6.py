''' ip: 5 3.8 7 5.6 4 2 3
op:15 6 9.4'''
a=list(map(input().split()))
even,odd,float=0,0,0
for i in a:
    if(i%2 == 0):
        even=i+even
    elif(i%2 == 1):
        odd=i+odd
    else:
        float=i+float
print(even)
print(odd)
print(float)
    