# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        arr = []
        for i in lists:
            head = i
            while head:
                arr.append(head.val)
                head = head.next
        
        arr.sort()

        new = ListNode(0)
        final = new

        for i in range(len(arr)):
            new.next = ListNode(arr[i])
            new = new.next

        return final.next