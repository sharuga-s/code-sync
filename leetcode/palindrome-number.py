class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x_str = str(x)
        lst = list(x_str)

        while len(lst) != 0:
            if lst[0] != lst[len(lst)-1]:
                return False
            lst = lst[1:len(lst) - 1]

        return True