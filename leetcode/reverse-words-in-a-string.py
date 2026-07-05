class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []

        temp = s.split(" ")

        for i in temp:
            if i != "":
                stack.append(i)

        final = ""
        stack.reverse()
        for i in range(len(stack)):
            final += stack[i] + " "

        return final.strip()