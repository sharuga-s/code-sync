# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        return self.isMirror(root.right, root.left)

    def isMirror(self, r, l):

        if not r and not l:
            return True

        if not r or not l:
            return False

        return (r.val == l.val) and self.isMirror(r.right, l.left) and self.isMirror(r.left, l.right)

# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: bool
#         """
        # left = self.treeToArr(root.left, [], True)
        # right = self.treeToArr(root.right, [], False)

        # return left == right

    # def treeToArr(self, root, arr, mirror):
    #     if not root:
    #         arr.append(None)
    #         return arr

    #     arr.append(root.val)
    #     print(arr)
        
    #     if mirror:
    #         self.treeToArr(root.right, arr, True)
    #         self.treeToArr(root.left, arr, True)
    #     else:
    #         self.treeToArr(root.left, arr, False)
    #         self.treeToArr(root.right, arr, False)
    #     return arr