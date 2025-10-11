
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None



class Solution:
    def insertAtPos(self, head, p, x):
        # Code Here
        curr = head
        
        for i in range(p):
            curr = curr.next
        
        newNode = Node(x)
        
        newNode.next = curr.next
        curr.next = newNode
        newNode.prev = curr.next.prev
        curr.next.prev = newNode
        
        return head
        
        