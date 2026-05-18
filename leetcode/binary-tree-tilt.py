# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.tilt_total = 0

        self.subTreeSum(root)

        return self.tilt_total
        
    def subTreeSum(self, root):
        if not root:
            return 0

        left = self.subTreeSum(root.left)
        right = self.subTreeSum(root.right)

        self.tilt_total += abs(left - right)

        return root.val + left + right

    ## redo with dfs!