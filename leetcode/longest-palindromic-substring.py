class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        maxstr = ""

        for i in range(len(s)):
            l1 = i
            r1 = i
            s1 = self.expand(l1, r1, s)


            # we need both -- i.e. "cbbd" would output 'c', but we expect 'bb'
            l2 = i
            r2 = i + 1
            s2 = self.expand(l2, r2, s)

            if len(s1) > len(maxstr):
                maxstr = s1
            
            if len(s2) > len(maxstr):
                maxstr = s2

        return maxstr

    def expand(self, l, r, s):
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            l -=1
            r += 1
        
        return s[l+1:r]
        
    #     for i in range(len(s) - 1, -1, -1):
    #         for j in range(len(s) - i):
    #             curr = s[j:i + j + 1]
    #             if self.isPalindrome(curr):
    #                 return curr

    #     return s

    # def isPalindrome(self, st):
    #     for i in range(len(st)//2):
    #         if st[i] != st[len(st) - i - 1]:
    #             return False

    #     return True