# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        return self.build(0, len(nums) - 1, nums)
        
    def build(self, low: int, high: int, nums: List[int]) -> Optional[TreeNode]:

        if low > high:
            return None

        mid = (low + high) // 2

        node = TreeNode(nums[mid])

        node.left = self.build(low, mid - 1, nums)
        node.right = self.build(mid + 1, high, nums)

        return node