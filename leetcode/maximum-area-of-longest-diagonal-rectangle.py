class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """

        maxdiag = 0
        maxarea = 0

        for i in dimensions:

            curr = sqrt(i[0] * i[0] + i[1] * i[1])

            if curr > maxdiag:
                maxarea = i[0] * i[1]
                maxdiag = curr
            elif curr == maxdiag:
                maxarea = max(maxarea, i[0] * i[1])
        
        return maxarea