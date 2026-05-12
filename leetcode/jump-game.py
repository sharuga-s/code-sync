class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_len = 0
        
        for i in range(len(nums)):
            if i > max_len:
                return False

            max_len = max(max_len, i + nums[i])

        return True