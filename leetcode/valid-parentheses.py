class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        parmap = {"(":")", "{":"}", "[":"]"}

        seen = []

        for i in range(len(s)):

            if s[i] in parmap:
                seen.append(s[i])

            else:
                if not seen or parmap[seen[-1]] != s[i]:
                    return False

                seen.pop()
                
        return not seen