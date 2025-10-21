# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        L1 = []
        L2 =[]

        currA = headA
        while currA is not None:
            L1.append(currA)
            currA = currA.next

        currB = headB
        while currB is not None:
            L2.append(currB)
            currB = currB.next
        
        lengthA = len(L1)
        lengthB = len(L2)

        small = (L1 if lengthA <= lengthB else L2)
        large = (L1 if lengthA >= lengthB else L2)

        if small == L1:
            smallname = 'A'
            bigname = 'B'
        else:
            smallname = 'B'
            bigname = 'A'

        count = 0
        for i in range(len(small) - 1, -1 , -1):
            if small[i] == large[i]:
                count += 1
            else:
                break
        
        if count == 0:
            return None
        else:
            len_to_trav = len(small) - count
            head = (headA if smallname == 'A' else headB)

            while len_to_trav > 0:
                head = head.next
                len_to_trav -= 1
            
            return head