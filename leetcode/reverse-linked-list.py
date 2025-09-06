# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        temp = ListNode()
        new = temp

        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        for i in range(len(arr)-1, -1, -1):
            new.next = ListNode(arr[i])
            new = new.next

        return temp.next