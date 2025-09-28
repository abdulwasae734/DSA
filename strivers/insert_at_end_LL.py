
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        curr = head
        while curr.next != None:
            curr = curr.next
        
        curr.next = Node(x)
        return head
            
        