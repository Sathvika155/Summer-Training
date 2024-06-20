
'''n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
'''
def palindrome(n,t):
    rev=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if(t==rev):
        return rev
    else:
        return palindrome(t+1,t+1)
n=int(input())
t=n
a=palindrome(n,t)
print(a)