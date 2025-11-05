# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """

        arr = []
        self.dfs(root, "", arr)
        return arr
        
    def dfs(self, root, s, arr):
        if not root:
            return
        
        if s:
            s += "->"
        s += str(root.val)
        
        # only append to arr if ur fr at the end
        if not root.left and not root.right:
            arr.append(s)
            return

        self.dfs(root.left, s, arr)
        self.dfs(root.right, s, arr)