class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        final = [[1]]

        for i in range(1, numRows):
            arr = [1]
            prev = final[i - 1]

            for j in range(1, len(prev)):
                arr.append(prev[j-1] + prev[j])

            arr.append(1)

            final.append(arr)

        return final