# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        curri = head
        currj = head.next

        if currj.next is None:
            if curri.val<currj.val:
                return head
            else:
                curri.val, currj.val = currj.val,curri.val
                return curri



        while curri.next is not None:
            temp = curri
            currj = curri.next

            while currj is not None:
                if currj.val < temp.val:
                    temp = currj
                currj = currj.next
            if temp != curri:
                curri.val, temp.val=temp.val, curri.val




            curri = curri.next

        return head
