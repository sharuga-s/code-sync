class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        s = ""

        for i in range(len(strs[0])):
            for j in strs[1:]:
                if i >= len(j) or j[i] != strs[0][i]:
                    return s
            
            s += strs[0][i]

        return s