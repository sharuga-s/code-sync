class Solution:
    def sortVowels(self, s: str) -> str:
        
        lst = list(s)

        vowels = []

        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                vowels.append(s[i])

        vowels.sort()

        # for i in range(len(idxs)):
        #     s = s[:idxs[i]] + lts[i] + s[idxs[i] + 1:]
        # splicing is costly for runtime

        vidx = 0

        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                lst[i] = vowels[vidx]
                vidx += 1

        # return s

        return "".join(lst)