class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        candies = [1] * len(ratings)
        
        # L to R
        for i in range(1, len(ratings)):
            if (ratings[i] > ratings[i - 1]):
                candies[i] = candies[i - 1] + 1

        # R to L --> the first loop only compares indexes to their left neighbours
        for i in range(len(ratings) - 2, -1, -1):
            if (ratings[i] > ratings[i + 1]):
                candies[i] = max(candies[i], candies[i + 1] + 1)
            
        return sum(candies)