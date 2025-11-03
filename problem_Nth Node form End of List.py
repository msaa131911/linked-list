class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
p1=Node(1)
p2=Node(2)
p3=Node(3)
p4=Node(4)
p5=Node(5)
p1.next=p2
p2.next=p3
p3.next=p4
p4.next=p5
head=p1
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = Node(0)
        dummy.next = head
        fast = slow = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next

s=Solution()
res = s.removeNthFromEnd(p1, 2)

while res:
    print(res.data, end=" ")
    res = res.next

