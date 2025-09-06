class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # sort = nums
        # rot = 0

        # for i in range(0, len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         sort = nums[i + 1:] + nums[:i + 1]
        #         rot = i + 1
        #         break
        
        # print(sort)
        # print(rot)

        # idx = -1

        low = 0
        hi = len(nums) - 1
        mid = (low + hi) // 2


        # while low <= hi:

        #     if sort[mid] == target:
        #         idx = (mid + rot) % len(nums)
        #         break
        #     if sort[low] == target:
        #         idx = (low + rot) % len(nums)
        #         break
        #     if sort[hi] == target:
        #         idx = (hi + rot) % len(nums)
        #         break

        #     if target < sort[mid]:
        #         hi = mid - 1
        #         mid = (low + hi) // 2
        #         continue
            
        #     else:
        #         low = mid + 1
        #         mid = (low + hi) // 2

        # return idx
            
        low = 0
        hi = len(nums) - 1

        while low <= hi:
            mid = (low + hi) // 2

            if nums[mid] == target:
                return mid

        # check if the left side is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target < nums[mid]:
                    hi = mid - 1
                else:
                    low = mid + 1

            # if left side isn't sorted, the right side must be
            else:
                if nums[mid] < target and target <= nums[hi]:
                    low = mid + 1
                else:
                    hi = mid - 1

        return -1