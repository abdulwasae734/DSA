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
            curr.next = newNode # type: ignore
            newNode.prev = curr # type: ignore
            curr = curr.next # type: ignore
        return head