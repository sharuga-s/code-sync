class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        stack = []
        final = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                 idx = stack.pop()
                 final[idx] = i - idx

            stack.append(i)

        return final