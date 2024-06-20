class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binary_Search:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.recursive_insert(self.root,data)
            
    def recursive_insert(self,node,data):
        if data<node.data:
            if node.left==None:
                node.left=data
            else:
                self.recursive_insert(node.left,data)
        elif data>node.data:
            if node.right==None:
                node.right=data
            else:
                self.recursive_insert(node.right,data)
b1=Binary_Search()
b1.insert(50)
b1.insert(60)
b1.insert(10)
                
        
        