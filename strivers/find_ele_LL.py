'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        #Code here
        curr = head
        
        while curr != None:
            if curr.data == key:
                return True
            curr = curr.next
        return False
        