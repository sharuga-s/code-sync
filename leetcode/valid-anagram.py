class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        hm = {}
        for i in s:
            if i not in hm:
                hm[i] = 0
            hm[i] += 1

        for i in t:
            if i not in hm:
                return False
            hm[i] -= 1

        for i in hm:
            if hm[i] != 0:
                return False

        return True