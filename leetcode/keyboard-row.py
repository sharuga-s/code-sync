class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"

        result = []

        for i in words:
            in1 = False
            in2 = False
            in3 = False
            for j in i.lower():
                if j in r1:
                    in1 = True
                elif j in r2:
                    in2 = True
                else:
                    in3 = True

            if not ((in1 and in2) or (in1 and in3) or (in2 and in3) or (in1 and in2 and in3)):
                result.append(i)

        return result