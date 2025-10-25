class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """

        per_7 = 28

        weeks = n / 7
        left = n % 7

        total = 0
        start = 1

        for i in range(weeks):
            total += sum(range(start, 7 + start))
            start += 1

        total += sum(range(start, left + start))

        return total