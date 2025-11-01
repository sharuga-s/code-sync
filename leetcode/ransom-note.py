class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        magmap = {}
        for i in magazine:
            if i not in magmap:
                magmap[i] = 0
            magmap[i] += 1

        for i in ransomNote:
            if i not in magmap or magmap[i] == 0:
                return False

            magmap[i] -= 1

        return True