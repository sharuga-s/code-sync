class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr_total = 0
        max_total = sum(nums)

        for i in nums:
            curr_total = max(i, i + curr_total)
            max_total = max(max_total, curr_total)
        
        return max_total