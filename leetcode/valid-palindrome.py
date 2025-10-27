class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Two pointer strat, the other is way too slow

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
        
            if (s[l].lower() != s[r].lower()):
                return False
            
            l += 1
            r -= 1
        
        return True
        
        # for i in range(len(s)):
        #     if ((s[i] >= "A" and s[i] <= "Z") or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= "0" and s[i] <= "9")):
        #         final += s[i]

        # for i in range(len(final)):
        #     if (final[i].lower() != final[len(final) - i - 1].lower()):
        #         return False

        # return True