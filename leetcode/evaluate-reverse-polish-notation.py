class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        final = 0

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())

            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                
                # we need the quotient to trunucate towards zero
                stack.append(int(float(a) / b))
            else:
                stack.append(int(i))

        return stack[0]