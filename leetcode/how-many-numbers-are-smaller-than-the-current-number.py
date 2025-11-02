class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        map = {}

        temp = sorted(nums)
        
        for i in range(len(temp)):
            if temp[i] not in map:
                map[temp[i]] = i

        result = []

        for i in nums:
            result.append(map[i])

        return result