class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True

            else:
                seen[nums[i]] = i

        return False
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, min(len(nums), i + k + 1)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False