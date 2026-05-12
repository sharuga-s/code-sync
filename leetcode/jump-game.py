class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # max_len is the farthest index you can possibly reach given all the jumps you've made so far.
        # greedy bc we always jump the max
        max_len = 0
        
        for i in range(len(nums)):
            if i > max_len:
                return False

            max_len = max(max_len, i + nums[i])

        return True