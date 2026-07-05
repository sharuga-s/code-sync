# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        lst = []

        while head:
            lst.append(head.val)
            head = head.next

        sortedLst = sorted(lst)

        final = ListNode(None)
        headfinal = final

        for i in sortedLst:
            final.next = ListNode(i)
            final = final.next

        return headfinal.next