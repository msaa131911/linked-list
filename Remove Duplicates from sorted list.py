class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(2)
b=node(2)
c=node(3)
d=node(5)
e=node(5)
f=node(5)
g=node(7)
h=node(8)
i=node(8)
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=g
g.next=h
h.next=i
head=a
class solution:
    def removeDuplicates(self,head):
        curr=head
        while curr !=None and curr.next!=None:
            if curr.data==curr.next.data:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head
s=solution()
res=s.removeDuplicates(head)
while res:
    print(res.data,end=" ")
    res=res.next