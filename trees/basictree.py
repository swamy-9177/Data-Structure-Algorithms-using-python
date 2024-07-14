class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Trees:
    def __init__(self):
        self.root=None
    def insert(self,value):
        newnode=Node(value)
        if not self.root:
            self.root=newnode
        else:
            curr=self.root
            while True:
                if curr.data>value:
                    if curr.left==None:
                        curr.left=newnode
                        break
                    else:
                        curr=curr.right
                else:
                    if curr.right==None:
                        curr.right=newnode
                        break
                    else:
                        curr=curr.right
    def preorder(self):
        self.helper(self.root)
    def helper(self,root):
        if root:
            print(root.data)
            self.helper(root.left)
            self.helper(root.right)
    def inorder(self):
        self.inhelper(self.root)
    def inhelper(self,root):
        if root:
            self.helper(root.left)
            print(root.data)
            self.helper(root.right)
t=Trees()
t.insert(5)
t.insert(3)
t.insert(4)
t.insert(1)
t.preorderd()
t.inorder()



















'''a=Node(1)'''
'''a.left.data=Node(2)
a.right.data=Node(3)
print(a.data)
print(a.left.data)
print(a.right.data)
'''
