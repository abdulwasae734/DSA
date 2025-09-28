'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        curr = head
        length = 1
        while curr.next != None:
            curr = curr.next
            length += 1
        
        return length