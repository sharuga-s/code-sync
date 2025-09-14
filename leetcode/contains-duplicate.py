class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # map = {}

        # for i in nums:
        #     if i in map:
        #         map[i] += 1
        #     else:
        #         map[i] = 1

        # for i in map:
        #     if map[i] > 1:
        #         return True

        # return False

        #______________________

        # using a set() is much faster
        # less passes/checks
        
        seen = set()

        for i in nums:
            if i in seen:
                return True

            seen.add(i)

        return False