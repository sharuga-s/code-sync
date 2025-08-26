class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max = 0
        # for i in range(0, len(height)):
        #     for j in range(i + 1, len((height))):
        #         if (abs(j - i) * min(height[j], height[i])) > max:
        #             max = abs(j - i) * min(height[j], height[i])
        
        # return max
        

        maxarea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            width = r - l
            h = min(height[l], height[r])
            maxarea = max(maxarea, width * h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxarea