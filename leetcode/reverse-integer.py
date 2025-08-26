class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        negative = False
        if x < 0:
            negative = True
            x = x * -1

        length = 0
        temp = x
        while temp >= 10:
            length += 1
            temp = temp / 10
        
        final = 0
        while length >= 0:
            final += (x % 10) * (10 ** length)
            length -= 1
            x = x / 10

        if negative:
            final = final * -1

        if (final > -(2 ** 31) and final < (2 ** 31)):
            return final
        return 0