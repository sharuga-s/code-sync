class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        first = self.binSearchForward(nums, 0, len(nums)//2, len(nums) - 1, target)

        last = self.binSearchBackward(nums, 0, len(nums)//2, len(nums) - 1, target)

        return [first, last]


    def binSearchForward(self, nums, l, mid, h, target):

        if l > h:
            return -1

        if nums[l] == target:
            return l

        if nums[mid] == target:
            left = self.binSearchForward(nums, l, (l + mid - 1)//2, mid - 1, target)
            return mid if left == -1 else left

        # we don't check if nums[h] == the target bc we want the leftmost val

        if target < nums[mid]:
            return self.binSearchForward(nums, l, (l + mid - 1)//2, mid - 1, target)

        return self.binSearchForward(nums, mid + 1, (mid + h + 1)//2, h, target)
        
    def binSearchBackward(self, nums, l, mid, h, target):

        if l > h:
            return -1

        if nums[mid] == target:
            right = self.binSearchBackward(nums, mid + 1, (h + mid + 1)//2, h, target)
            return mid if right == -1 else right

        if nums[h] == target:
            return h

        if target > nums[mid]:
            return self.binSearchBackward(nums, mid + 1, (mid + h + 1)//2, h, target)

        return self.binSearchBackward(nums, l, (l + mid - 1)//2, mid - 1, target)