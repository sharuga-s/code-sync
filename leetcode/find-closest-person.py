class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """

        closest = min(abs(z - x), abs(z - y))

        if closest == abs(z-x) and closest == abs(z-y):
            return 0
        elif closest == abs(z-x):
            return 1
        
        return 2