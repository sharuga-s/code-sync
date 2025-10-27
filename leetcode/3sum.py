class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        
        final = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            if (i > 0 and nums[i] == nums[i - 1]):
                continue
                #ignore, we already checked this combo

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    final.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return final