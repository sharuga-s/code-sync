class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        hm = {}

        for i in s:
            if i not in hm:
                hm[i] = 0

            hm[i] += 1

        for i in range(len(s)):
            if hm[s[i]] == 1:
                return i

        return -1