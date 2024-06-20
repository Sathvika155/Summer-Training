'''n=int(input())
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")'''
def palindrome(n,rev):
    if (n==0):
        return rev
    rem=n%10
    rev = (rev * 10) + rem
    return palindrome((n// 10), rev)
n=int(input())
rev=0
p=palindrome(n,rev)
if(n==p):
    print("yes")
else:
    print("no")


    