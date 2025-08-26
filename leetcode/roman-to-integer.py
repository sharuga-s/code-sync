class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = list(s)
        count = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                if i + 1 < len(s) and s[i + 1] == "V":
                    count += 4
                    i = i + 2
                elif i + 1 < len(s) and s[i + 1] == "X":
                    count += 9
                    i = i + 2
                else:
                    count += 1
                    i += 1
            elif s[i] == "V":
                count += 5
                i += 1
            elif s[i] == "X":
                if i + 1 < len(s) and s[i + 1] == "L":
                    count += 40
                    i = i + 2
                elif i + 1 < len(s) and s[i + 1] == "C":
                    count += 90
                    i = i + 2
                else:
                    count += 10
                    i += 1
            elif s[i] == "L":
                count += 50
                i += 1
            elif s[i] == "C":
                if i + 1 < len(s) and s[i + 1] == "D":
                    count += 400
                    i = i + 2
                elif i + 1 < len(s) and s[i + 1] == "M":
                    count += 900
                    i = i + 2
                else:
                    count += 100
                    i += 1
            elif s[i] == "D":
                count += 500
                i += 1
            elif s[i] == "M":
                count += 1000
                i += 1
        return count