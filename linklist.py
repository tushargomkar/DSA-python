# The manual way of linklist 
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next




Head=Node(1)
A=Node(2)
B=Node(31)
C=Node(4)

Head.next=A
A.next=B
B.next=C

def printF(head):
    i = head
    while i is not None:
        print(i.value)
        i = i.next
printF(Head)