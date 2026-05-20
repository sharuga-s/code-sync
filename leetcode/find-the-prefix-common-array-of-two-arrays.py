class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        c = [0] * len(A)

        if A[0] == B[0]:
            c[0] += 1

        for i in range(1, len(A)):
            c[i] = c[i - 1]
            if A[i] in B[:i+1]:
                c[i] += 1
            if B[i] in A[:i]:
                c[i] += 1

        return c