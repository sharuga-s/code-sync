class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        best = 0
        # set is super fast
        nums = set(nums)

        for i in nums:
            if (i - 1) not in nums:
                y = i + 1
                curr_len = 0
                while y in nums:
                    curr_len += 1
                    y = y + 1
                best = max(best, curr_len)

        return best + 1

        # if not nums:
        #     return 0

        # nums.sort()

        # count = 0
        # max_count = 0

        # print(nums)

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         continue
        #     if (nums[i] - nums[i - 1]) == 1:
        #         count += 1
        #         print(count)
        #         print(max_count)
        #         if count > max_count:
        #             max_count = count

        #     else:
        #         count = 0

        # return max_count + 1