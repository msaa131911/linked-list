class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(10)
b=node(20)
c=node(30)
a.next=b
b.next=c

hade=a
def traverse_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next
#insert add to 1st
d=node(40)
d.next=hade
hade=d

#insert add to last
e=node(1)
curr=hade
while curr.next is not None:
    curr=curr.next
curr.next=e

#insert add to middle
k=2
f=node(2)
curr=hade 
for i in range(k-1):
    curr=curr.next
f.next=curr.next
curr.next=f


traverse_linked_list(hade)
