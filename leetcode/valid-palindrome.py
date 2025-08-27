class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()
        new = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                new += s[i]

        while len(new) > 1:
            if new[0] != new[-1]:
                return False
            new = new[1:-1]
        return True