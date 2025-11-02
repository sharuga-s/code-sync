class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        return nums[len(nums) // 2]

        # hm = {}

        # for i in nums:
        #     if i not in hm:
        #         hm[i] = 0
        #     hm[i] += 1

        #     if hm[i] > len(nums) / 2:
        #         return i

        # return -1