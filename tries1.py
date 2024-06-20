class node:
    def _init_(self):
        self.d={}
        self.flag=0
        self.count={}
class tries:
    def _init_(self):
        self.root=node()
    def insert(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                t.d[i]=node() 
            t=t.d[i]
        t.flag=1
    def word_search(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
    def prefix_search(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    def prefix_words(self,str1):
        def fun(t,s):
            if(t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str1:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
    '''def prefix_count(self,str1):
        def fun(t,s):
            if(t.flag==1):
                count=count+1
                print(c)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str1:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)'''
    def largest_prefix(self,str1):
        l=[]
        def fun(t,s):
            if(t.flag==1):
                p=len(s)
                l.append(s)
               
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str1:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
        print(l)
        
t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.word_search(s))
    if(a=='3'):
        print(t1.prefix_search(s))
    if(a=='4'):
        t1.prefix_words(s)
    if(a=='5'):
        t1.largest_prefix(s)