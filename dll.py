class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,data):
        if(self.head==None):
            self.head=node(data)
            self.tail=self.head
        else:
            t=node(data)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
    def addbegin(self,data):
        if(self.head==None):
            self.head=node(data)
            self.tail=None
        else:
            t=node(data)
            self.head.prev=t
            t.next=self.head
            self.head=self.head.prev
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="<->")
            t=t.next
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="<->")
            t=t.prev
    def linearsearch(self,target):
        t=self.head
        q=self.tail
        flag=0
        while(t!=q and t!=q.next):
            if(t.data==target or q.data==target):
                print('found')
                break
            else:
                t=t.next
                q=q.prev
    def evenodd(self):
        t=self.head
        q=self.tail
        flag=0
        while(t!=None and q!=None):
            if(t==q):
                flag=1
                print('odd')
                break
            else:
                t=t.next
                q=q.prev
        if(flag==0):
            print('even')
    def palindrome(self):
        t=self.head
        q=self.tail
        flag=0
        while(t!=q and t!=q.next):
            if(t.data!=q.data):
                flag=1
            else:
                flag=0
                break
            t=t.next
            q=q.prev
        if(flag==1):
            print('palindrome')
        else:
            print('not palindrome')
    def evendisp(self):
        t=self.head
        q=self.tail
        while(t.next!=q):
            t=t.next
            q=q.prev
        t=self.head
        while(q!=None):
            temp=node(t.data)
            t.data=q.data
            q.data=temp.data
            t=t.next
            q=q.next
    def validparenthesis(self):
        flag=0
        count=0
        stack=[]
        i=self.head
        while(i!=None):
            if i.data in ["(","{","["]:
                stack.append(i.data)
                count=count+1
            else:
                if not stack:
                    if(i.data == '}' and stack[-1]=='{' or i.data == ']' and stack[-1]=='[' or i.data == ')' and stack[-1]=='('):
                        stack.pop()
                        count=count+1
                    else:
                        f=1
                        break
                else:
                    f=1
                    break
            i=i.next
        if(flag==1):
            print('no')
        else:
            print('yes')
        print(count)
    def evenoddrecursion(self,t,es,os):
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.evenoddrecursion(t.next,es,os)
        
            
l1=dll()
l1.addback(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(55)
l1.display()
print()
a=l1.evenoddrecursion(l1.head,0,0)
print(a)
        
        