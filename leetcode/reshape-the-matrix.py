class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        if r * c != len(mat) * len(mat[0]):
            return mat
            # we can't allocate properly in this case

        total = []
        new = []
        for i in mat:
            for j in i:
                total.append(j)

        for i in range(r):
            print(total[i*c:i*c+c])
            new.append(total[i*c:i*c+c])   

        return new