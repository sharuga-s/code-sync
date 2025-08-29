# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        curr = head
        arr = []
        i = 0
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        for i in range(0, len(arr)):
            if i == len(arr) - n:
                arr = arr[:i] + arr[i + 1:]
                break
                
        if not arr:
            return None

        new = ListNode(arr[0])
        tail = new
        for i in range(1, len(arr)):
            tail.next = ListNode(arr[i])
            tail = tail.next
        
        return new