class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def addbegin(self,data):
        if(self.head==None):
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def addback(self,data):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(data)
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def addeven(self):
        s=0
        t=self.head
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
                t=t.next
        print(s)
    def delbegin(self):
        if(self.head==None):
            return
        self.head=self.head.next
        del self.head
    def search(self,target):
        flag=0
        t=self.head
        while t!=None:
            if(t.data==target):
                print('found')
                flag=1
                break
            else:
                t=t.next
        if(flag==0):
            print('not found')
    def middlenode(self):
        slow_pointer=self.head
        fast_pointer=self.head
        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer=fast_pointer.next.next
            slow_pointer=slow_pointer.next
        print(slow_pointer.data)
    def pairs(self):
        slow_pointer=self.head
        fast_pointer=self.head.next
        while slow_pointer.next is not None:
            while fast_pointer is not None:
                print(slow_pointer.data,",",fast_pointer.data)
                fast_pointer=fast_pointer.next
            slow_pointer=slow_pointer.next
            fast_pointer=slow_pointer.next
    def sequencecount(self):
        maxcount=0
        count=0
        t=self.head
        while(t.next!=None):
            if((t.data)+1 == t.next.data):
                count=count+1
            else:
                if(count>maxcount):
                    maxcount=count
                count=1
            t=t.next
        if(count>maxcount):
            maxcount=count
        print(maxcount)
    def bubblesort(self):
        count=0
        T=self.head
        p=None
        while(T.next!=None):
            t=self.head
            flag=0
            while(t.next!=p):
                if(t.data>t.next.data):
                    flag=1
                    t.data=t.next.data
                    t.next.data=t.data
                t=t.next
                count=count+1
            if(flag==0):
                break
            return count
            p=t
            T=T.next
            
               
               
l1=sll()
l1.addbegin(1)
l1.addback(3)
l1.addback(2)
l1.addback(7)
l1.addback(6)
l1.addback(5)
l1.display()
print()
l1.search(10)
l1.middlenode()
l1.pairs()
l1.sequencecount()
b=l1.bubblesort()
l1.display()
print()
print(b)

