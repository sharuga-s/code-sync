class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]

        # return []

        intmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in intmap:
                return [i, intmap[complement]]
            
            intmap[nums[i]] = i

        return []