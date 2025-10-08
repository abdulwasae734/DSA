#User function Template for python3

# Node Class
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

         
        
class Solution:
    def constructDLL(self, arr):
        # Code here
        
        head = Node(arr[0])
        
        curr = head
        
        for i in range(1, len(arr)):
            newNode = Node(arr[i])
            curr.next = newNode
            newNode.prev = curr
            curr = curr.next
        return head