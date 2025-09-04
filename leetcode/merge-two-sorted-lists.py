# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head1 = list1
        head2 = list2

        # you need a variable to point at its head, and another variable to actually edit it
        ref = ListNode()
        new = ref

        while head1 and head2:
           
            if head1.val < head2.val:
                new.next = head1
                head1 = head1.next

            else:
                new.next = head2
                head2 = head2.next

            new = new.next
        
        if head2:
            new.next = head2
        
        if head1:
           new.next = head1
        
        return ref.next