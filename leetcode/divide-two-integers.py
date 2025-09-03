class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # using powers of two to do subtraction faster
        # uses solution

        if dividend == divisor:
            return 1

        if divisor == 1:
            return dividend
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        n, d = abs(dividend), abs(divisor)
        ans = 0

        while n >= d:
            p = 0
            while n >= (d << p):
                p += 1
            
            p -= 1
            n -= (d << p)
            ans += (1 << p)

        if sign < 0:
            ans = -ans
        return min(max(ans, -2**31), 2**31 - 1)