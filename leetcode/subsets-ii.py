class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = [[]]
        nums.sort()
        
        self.dfs(0, [], nums, result)

        return result
        
    def dfs(self, idx, arr, nums, result):
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            sub = arr + [nums[i]]
            result.append(sub)
            self.dfs(i + 1, sub, nums, result)