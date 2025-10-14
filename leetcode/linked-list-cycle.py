# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        a = head
        b = head

        while a and b and b.next:
            a = a.next
            b = b.next.next

            # if the list is cyclical, a and b are bound to match up at one point (b will catch up to a)

            if a == b:
                return True


        return False