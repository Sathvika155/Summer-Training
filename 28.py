'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(10)
b=node(20)
c=node(30)
a.next=b
b.next=c
This creates a link between a and b ie 10->20->30->None
print(a.data,a.next)
print(b.data,b.next)
print(c.data,c.next)
_________________________________________________________________________________________________________
'''
class node:
    def__init__(self,data):
        self.data=data
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
t=head
while(t!=None):
    print(t.data)
    t=t.head
'''
print(head)
print(head.next)'''

