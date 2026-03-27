#singly linked list

class node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
#linked list
class linkedlist:
    #constructor
    def __init__(self,head=None):
        self.head=head
     #insert end method
    def insert_end(self,value):
        new_node=node(value)
        if self.head is None:
            self.head=new_node
        else:
            t1=self.head
            while t1.next is not None:
                t1=t1.next
            t1.next=new_node

    #insert begining
    def insert_begining(self,value):
      temp=node(value)
      temp.next=self.head
      self.head=temp

     #insert middle
    def insert_medile(self,value,x):
        new_node=node(value)
        t1=self.head
        while t1.next is not None:
            if t1.data==x:
                new_node.next=t1.next
                t1.next=new_node
            t1=t1.next
     #delete
    def delete(self,value):
        t1=self.head
        prev=t1
        if t1.data==value:
            self.head=t1.next
        while t1.next is not None:
            if t1.data==value:
                prev.next=t1.next
                break
            else:
                prev=t1
                t1=t1.next  
        if t1.data==value:
            prev.next=None

    #display
    def display(self):
        t1=self.head
        while t1 is not None:
            print(t1.data)
            t1=t1.next


n=linkedlist()
n.insert_end(10)
n.insert_end(20)
n.insert_end(30)
n.insert_end(40)
n.insert_end(50)
n.insert_begining(5)
n.insert_medile(25,30)
n.delete(50)
n.display()