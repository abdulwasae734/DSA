"""
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        # code here
        prev = None
        curr = head
        
        
        for i in range(x-1):
            prev = curr
            curr = curr.next
            
        
        if curr.next != None:
            prev.next = curr.next
            curr.next.prev = curr.prev
        else:
            prev.next = None
        return head
        