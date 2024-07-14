'''class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None
a=Node(1)
b=Node(2)
c=Node(3)
a.next=b
b.next=c
print(a.data)
print(a.next.data)
print(a.next.next.data)'''
'''class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertatbegin(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next

a=LinkedList()
a.insertatbegin(1)
a.insertatbegin(2)
a.insertatbegin(3)
a.insertatbegin(4)
a.printlist()'''
class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertatbegin(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
    def insertatend(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            return
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newnode
    def printlist(self):
            cur=self.head
            while cur:
                print(cur.data,end="->")
                cur=cur.next
    def deleteatbeg(self):
        if not self.head:
            return
        else:
            self.head=self.head.next
    def deleteatend(self):
        if not self.head:
            return
        if self.head.next==None:
            self.head=None
        else:
            curr=self.head
            while curr.next.next!=None:
                curr=curr.next
            curr.next=None
    def printcount(self,value):
            c=1
            cur=self.head
            while cur.next:
                c+=1
                cur=cur.next
            print(c)
            m=c//2
            print(m)
            i=1
            curr=self.head
            #insertion at middle
            while i!=m+1:
                curr=curr.next
                i+=1
            print(curr.data)
            newnode=Node(value)
            newnode.next=curr.next
            curr.next=newnode
    def search(self,val):
        curr=self.head
        while curr!=None:
            if curr.data==val:
                print("yes")
                break
            curr=curr.next
        else:
            print("no")
    def searchin(self,val,data):
        curr=self.head
        newnode=Node(data)
        while curr:
            if curr.data==val:
                print("yes")
                newnode=curr.next
                curr.next=newnode
                break
            curr=curr.next
            else:
            print("no")
a=LinkedList()
a.insertatbegin(1)
a.insertatbegin(2)
a.insertatbegin(3)
a.insertatbegin(4)
a.insertatend(5)
a.searchin(3,7)
'''a.deleteatbeg()
a.deleteatend()
a.search(1)
a.printcount(8)'''
a.printlist()




