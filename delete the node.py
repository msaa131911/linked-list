class node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=node(1)
b=node(2)
c=node(3)
a.next=b
b.next=c
hade=a

def traverse(hade):
    curr=hade
    while curr is not None:
        print(curr.data)
        curr=curr.next

d=node(4)
d.next=hade
hade=d

e=node(5)
curr=hade
while curr.next is not None:
    curr=curr.next
    
curr.next=e

k=2
f=node(6)
curr=hade
for i in range(k-1):
    curr=curr.next
    
f.next=curr.next
curr.next=f

#delete last node
curr=hade
while curr.next.next is not None:
    curr=curr.next
    
curr.next=None

#delete node at maddle position
k=2
curr=hade
for i in range(k-1):
    curr=curr.next
    
curr.next=curr.next.next
traverse(hade)