class Solution:
    def intToRoman(self, num: int) -> str:
        
        map = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}

        final = ""

        for i in map:
            while num >= i:
                final += map[i]
                num -= i
        
        return final

        # final = ""

        # arr = {5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}

        # len = 0
        # temp = num

        # while temp > 0:
        #     temp //= 10
        #     len += 1

        # while num > 0:
            
        #     start = num // (10 ** (len - 1))
        #     startTotal = start * 10 ** (len - 1)
        #     num -= startTotal

        #     len -= 1

        #     if start != 4 and start != 9: