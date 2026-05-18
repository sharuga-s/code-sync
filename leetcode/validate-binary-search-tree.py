# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        return self.isValidMaxAndMin(root, None, None)

    def isValidMaxAndMin(self, node, max_val, min_val):

        if not node:
            return True
        
        # this case is just for the initial left and right children
        if min_val != None and node.val <= min_val:
            return False
        elif max_val != None and node.val >= max_val:
            return False

        # 1. going left, so the current node val is the max
        # 2. going right so the current node val is the min
        return self.isValidMaxAndMin(node.left, node.val, min_val) and self.isValidMaxAndMin(node.right, max_val, node.val)