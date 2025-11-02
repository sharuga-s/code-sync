class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        nummap = {}


        for i in arr1:
            if i not in nummap:
                nummap[i] = 0

            nummap[i] += 1

        result = []

        for i in arr2:
            result += [i] * nummap[i]
            nummap[i] = 0

        temp = []
        for i in nummap:
            if nummap[i] > 0:
                temp += [i] * nummap[i]

        temp.sort()

        result += temp

        return result