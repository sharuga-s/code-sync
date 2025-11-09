class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        lo = 0
        hi = len(matrix) * len(matrix[0]) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            val = matrix[row][col]

            if val == target:
                return True

            elif val < target:
                lo = mid + 1

            else:
                hi = mid - 1

        return False