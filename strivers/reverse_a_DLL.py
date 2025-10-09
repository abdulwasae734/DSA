"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        if not head:
            return None
            
        curr = head
        prev = None
        
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            
            prev = curr
            
            curr = curr.prev
        
        return prev
        