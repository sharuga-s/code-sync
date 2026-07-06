class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals.sort(key=lambda x: (x[0], -x[1]))

        max_r = 0
        final = 0

        for i in intervals:
            if not i[1] <= max_r:
                final += 1
            max_r = max(max_r, i[1])

        return final