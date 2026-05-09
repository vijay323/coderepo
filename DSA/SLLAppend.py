class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class SLL:
    def __init__(self):
        self.head=None
    
    def append(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode


n1=Node(5)

n2=Node(6)
n3=Node(7)

v1=SLL()
v1.append(8)

print(n3.next)