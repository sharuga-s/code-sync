class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        cols = len(matrix[0])
        rows = len(matrix)

        new = []

        for i in range(cols):
            curr = []
            for j in range(rows):
                curr.append(matrix[j][i])

            new.append(curr)

        return new