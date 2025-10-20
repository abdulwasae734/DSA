'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        arr = []
        temp = head
        
        
        
        while temp:
            arr.append(temp.data)
            temp = temp.next
        
        arr.sort()
        
        temp = head
        i = 0
        
        
        while temp:
            temp.data = arr[i]
            temp = temp.next
            
            i += 1
        
        return head
