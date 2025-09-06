class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxsum = nums[0]
        currsum = 0

        # for i in range(len(nums), 0, -1):
        #     for j in range(len(nums) - i + 1):
        #         curr = nums[j:i + j]
        #         currsum = sum(curr)
        #         if currsum > maxsum:
        #             maxsum = currsum
        #             maxarr = curr

        for i in nums:
            currsum = max(i, i + currsum)
            maxsum = max(maxsum, currsum)

        return maxsum