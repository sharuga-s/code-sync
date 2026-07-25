class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anamap = {}

        for i in strs:
            sort = "".join(sorted(i))
            if sort not in anamap:
                anamap[sort] = []

            anamap[sort].append(i)

        final = []

        for i in anamap:
            final.append(anamap[i])

        return final