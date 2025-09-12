class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        # as soon as there is a vowel in the string, Alice win's
        # if there's an odd number of vowels, she can remove the whole thing
        # if there's an even number of vowels, she can remove (n - 1) vowels, so Bob can't go, thus she wins

        if len(s) == 0:
            return False

        for i in s:
            if i in "AEIOUaeiou":
                return True

        return False