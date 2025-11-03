class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        result = 0
        for i in range(len(s)):
            curr = dic[s[i]]
            if i + 1 < len(s):
                nextval = dic[s[i + 1]]
            else:
                nextval = 0

            if curr < nextval:
                result -= curr

            else:
                result += curr

        return result