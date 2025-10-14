'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        loop = False
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                loop = True
                break
        
        if loop:
            curr = slow
            count = 1
            curr = curr.next
            while curr != slow:
                curr = curr.next
                count += 1
            return count
        else:
            return 0
                