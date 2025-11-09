class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        l = 1
        r = max(piles)

        while l < r:
            # try a mid speed
            m = (l + r) // 2
            total = 0

            # calculate how many hours it would take at speed = m
            for i in piles:
                # find how long each pile would take at speed m
                total += (i + m - 1) // m
            
            # speed is too slow
            if total > h:
                l = m + 1  # increase lower bound --> try faster speed
            else:
                # try slower speed
                r = m


        return l