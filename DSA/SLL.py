class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


node1 = Node(5)
node2 = Node(6)
node3 = Node(7)
 

node1.next=node2
node2.next=node3

print(node1.val)
print(node1.next)
print(node2)