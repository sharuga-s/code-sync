class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        word = ''.join(sorted(word))
        k = 0

        for i in range(len(word)):
            if word[i].islower():
                break
            if not word[i] == word[i-1] and word[i].lower() in word:
                k += 1
        return k