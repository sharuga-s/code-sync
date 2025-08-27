class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # BEATS 5.03%

        # s = s.lower()
        # new = ""
        # for i in range(len(s)):
        #     if s[i].isalpha() or s[i].isnumeric():
        #         new += s[i]

        # while len(new) > 1:
        #     if new[0] != new[-1]:
        #         return False
        #     new = new[1:-1]
        # return True

        # BEATS 10.09%

        news = ""
        for i in s:
            if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z' or i >= '0' and i <= '9':
                news += i
        s = news
        print(s)
        for i in range(len(s)):
            if s[i].lower() != s[len(s) - i - 1].lower():
                return False
        return True