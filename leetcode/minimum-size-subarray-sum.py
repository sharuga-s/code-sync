class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        min_arr_len = len(nums)
        curr_sum = 0

        left = 0

        for r in range(len(nums)):
            # local = curr_sum - nums[i]
            # if local >= target and (len(nums) - i) > min_arr_len:
            #     min_arr_len = len(nums) - i
            curr_sum += nums[r]

            while curr_sum >= target:
                min_arr_len = min(min_arr_len, r - left + 1)
                curr_sum -= nums[left]
                left += 1

        if min_arr_len == len(nums) and sum(nums) < target:
            return 0
        return min_arr_len