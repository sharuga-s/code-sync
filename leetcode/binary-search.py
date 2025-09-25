class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        hi = len(nums) - 1

        while low <= hi:
            mid = (low + hi) // 2

            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                hi = mid - 1
            
            else:
                low = mid + 1

        return -1