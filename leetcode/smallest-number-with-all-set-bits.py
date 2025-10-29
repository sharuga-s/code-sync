class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        x = 0
        i = 0
        while x < n:
            # we have that for all binary reps containing ONLY 1s, there's a pattern

            # 1111 -> (1×23)+(1×22)+(1×21)+(1×20) = 15 -> 2^4 - 1
            x = (2 ** i) - 1
            i += 1

        return x