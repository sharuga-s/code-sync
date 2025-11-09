class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxlen = 0
        seen = {}
        l = 0

        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= l:
                l = seen[s[i]] + 1

            seen[s[i]] = i
            maxlen = max(maxlen, i - l + 1)

        return maxlen