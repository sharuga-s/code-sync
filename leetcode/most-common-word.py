class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        hm = {}

        clean = ""
        for ch in paragraph:
            if ch.isalpha():
                clean += ch.lower()
            else:
                clean += " "  # replace punctuation with space

        # now safely split on spaces
        words = clean.split()

        for i in words:
            if i in banned:
                continue
            if i not in hm:
                hm[i] = 0
            hm[i] += 1

        maxl = 0
        word = ""
        for i in hm:
            if hm[i] > maxl:
                maxl = hm[i]
                word = i

        return word