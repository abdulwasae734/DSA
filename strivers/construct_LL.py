
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def arrayToList(self, arr):
        # code here
        head = None
        curr = None
        for i in arr:
            if not head:
                head = Node(i)
                curr = head
            else:
                newnode = Node(i)
                curr.next = newnode
                curr = curr.next
        
        return head
            
        
        