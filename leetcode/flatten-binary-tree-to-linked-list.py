# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if not root:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            tail = root.left
            while tail.right:
                tail = tail.right
            
            tail.right = root.right
            root.right = root.left
            root.left = None