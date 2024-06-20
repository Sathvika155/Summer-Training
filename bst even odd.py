class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)
                
    #INORDER TRAVERSAL
    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])
    
    def _inorder_traversal(self, current_node, result):
        if current_node:
            self._inorder_traversal(current_node.left, result)
            result.append(current_node.value)
            self._inorder_traversal(current_node.right, result)
        return result
    
    #PREORDER TRAVERSAL
    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])
    
    def _preorder_traversal(self, current_node, result):
        if current_node:
            result.append(current_node.value)
            self._preorder_traversal(current_node.left, result)
            self._preorder_traversal(current_node.right, result)
        return result
   
    
    def postorder_traversal(self):
        return self._postorder_traversal(self.root,[])
    
    def _postorder_traversal(self,current_node,result):
        if current_node:
            self._postorder_traversal(current_node.left,result)
            self._postorder_traversal(current_node.right,result)
            result.append(current_node.value)
        return result    
        
    def display(self):
        print(self.inorder_traversal())
        print(self.preorder_traversal())
        print(self.postorder_traversal())
        print(self.topview1()+self.topview2())
        
        
    def sum(self):
        values=self.inorder_traversal()
        sum=0
        for i in values:
            sum=sum+i
        print(sum)
        
        
    def sum1(self):
        return self._sum1(self.root)
    def _sum1(self, current_node):
        if current_node is None:
            return 0
        return current_node.value+self._sum1(current_node.left)+self._sum1(current_node.right)
    
    
    def evenodd(self):
        return self._evenodd(self.root)
    def _evenodd(self, current_node):
        if current_node is None:
            return 0
        if(current_node.value)%2 == 0:
            return current_node.value+self._evenodd(current_node.left)+self._evenodd(current_node.right)
        else:
            return self._evenodd(current_node.left)+self._evenodd(current_node.right)-current_node.value
        
        
    def height(self):
        return self._height(self.root)
    
    def _height(self,current_node):
        if current_node==None:
            return -1
        else:
            return max(self._height(current_node.left),self._height(current_node.right)+1)
        
        
    def balance(self):
        return self._balance(self.root)
    def _balance(self,current_node):
        if current_node==None:
            return -1
        else:
            return abs(self._balance(current_node.left)-self._balance(current_node.right))<=1
        
        
    def leafnode(self):
        return self._leafnode(self.root)
    def _leafnode(self,current_node):
        if current_node==None:
            return 0
        elif current_node.left==None and current_node.right==None :
            return 1
        return self._leafnode(current_node.left)+self._leafnode(current_node.right)
    
    
    def sum_leafnode(self):
        return self._sum_leafnode(self.root)
    def _sum_leafnode(self,current_node):
        if current_node==None:
            return 0
        elif current_node.left==None and current_node.right==None :
            return current_node.value
        return self._sum_leafnode(current_node.left)+self._sum_leafnode(current_node.right)
    
    
    def search(self,target):
        return self._search(self.root,target)
    def _search(self,current_node,target):
        if current_node==None:
            return "not found"
        if current_node.value==target:
            return "found"
        if target<current_node.value:
            return self._search(current_node.left,target)
        if target>current_node.value:
            return self._search(current_node.right,target)
    '''    
    def topview(self):
        return self._topview(self.root,[],[])
    def _topview(self,current_node,result1,result2):
        if current_node:
            self._topview(current_node.left,result1,result2+1)
            result1.append(current_node.value)
            result
        return result2
    def topview1(self):
        return self._topview1(self.root,[])
    def _topview1(self,current_node,result1):
        if current_node:
            self._topview1(current_node.right,result1)
            result1.append(current_node.value)
        return result1
    '''    '''
    def topview1(self):
        return self._topview1(self.root,[],c)
    def _topview1(self,current_node,result1,c):
        if current_node==None:
            return
        result1.append(current_node.value)
        result1.append(c)
        self._topview1(current_node.left,c+1)
        self._topview1(current_node.right,c+1)
    def topview2(self):
        return self._topview2(self.root,[],c)
    def _topview2(self,current_node,result1,c):
        if current_node==None:
            return
        result1.append(current_node.value)
        result1.append(c)
        self._topview2(current_node.right,c+1)
        self._topview2(current_node.left,c+1)
        '''
    def leftview(self):
        return self._leftview(self.root,[],0)
    def _leftview(self,current_node,result1,c):
        if(current_node==None):
            return
        if c not in result1:
            result1.append(c)
            print(current_node.value)
        self._leftview(current_node.left,result1,c+1)
        self._leftview(current_node.right,result1,c+1)
        

    def rightview(self):
        return self._leftview(self.root,[],0)
    def _rightview(self,current_node,result1,c):
        if(current_node==None):
            return
        if c not in result1:
            result1.append(c)
            print(current_node.value)
        self._rightview(current_node.right,result1,c+1)
        self._rightview(current_node.left,result1,c+1)
        
    def top_view(self):
        return self._top_view(self.root)
    def _top_view(self,current_node):
        if current_node==None:
            return
        d={}
        q=[(current_node,0)]
        while(q):
            current_node=q[0][0]
            if(current_node.left!=None):
                q.append(current_node.left,q[0][1]-1)
            if(current_node.right!=None):
                q.append(current_node.right,q[0][1]+1)
            if(q[0][1] not in d):
                d[q[0][1]]=current_node.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")
            
        
          
      
    
    
                     
        
    
    
        
bst = BinarySearchTree()
numbers = [10,2,5,7,20,21,25,30]
for i in numbers:
    bst.insert(i)
'''
bst.display()
p=bst.sum1()
print(p)
a=bst.evenodd()
print(abs(a))
b=bst.height()
print(b)
b=bst.balance()
print(b)
c=bst.leafnode()
print(c)
d=bst.sum_leafnode()
print(d)
e=bst.search(5)
print(e)
'''
'''bst.leftview()'''
a=bst.top_view()
print(a)
