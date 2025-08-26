# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodeToNum(self, node, count, total):
        if not node:
            return total
        return self.nodeToNum(node.next, count + 1, total + (10 ** count) * node.val)
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        total1 = self.nodeToNum(l1, 0, 0)
        total2 = self.nodeToNum(l2, 0, 0)

        total = total1 + total2
        if total == 0:
            return ListNode(0)

        final = ListNode(total % 10)
        total = total / 10
        curr = final
        while total > 0:
            curr.next = ListNode(total % 10)
            curr = curr.next
            total //= 10 

        return final