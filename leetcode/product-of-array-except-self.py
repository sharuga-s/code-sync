class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        total = 1
        zero_count = 0

        for i in nums:
            if i == 0:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)

        for i in nums:
            if i != 0:
                total *= i
        
        result = []
        for i in nums:
            if zero_count == 0:
                result.append(total // i)
            elif zero_count == 1:
                if i == 0:
                    result.append(total)
                else:
                    result.append(0)

        return result