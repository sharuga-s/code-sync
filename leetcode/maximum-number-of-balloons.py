class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        
        balmap = {"b":0, "a":0, "l":0, "o":0, "n":0}

        for i in text:
            if i in balmap:
                balmap[i] += 1

        count = 0
        
        x = min(balmap["b"], balmap["a"], balmap["n"])
        # if balmap["b"] >= x and balmap["a"] >= x and balmap["n"] >= x and balmap["l"] >= (2 * x) and balmap["o"] >= (2 * x):
        #     return x
        
        return min(balmap["l"] // 2, balmap["o"] // 2, x)