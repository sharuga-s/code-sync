class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        max = s[0]
        for i in range(len(s)):
            string = s[i]
            new = s[i+1:]
            for j in range(len(new)):
                if new[j] in string:
                    break
                string += new[j]
                if len(string) > len(max):
                    max = string
    
        return len(max)