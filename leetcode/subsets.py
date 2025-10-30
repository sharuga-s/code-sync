class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = [[]]
        
        self.dfs(0, [], nums, result)

        return result
        
    def dfs(self, idx, arr, nums, result):
        for i in range(idx, len(nums)):
            sub = arr + [nums[i]]
            result.append(sub)
            self.dfs(i + 1, sub, nums, result)