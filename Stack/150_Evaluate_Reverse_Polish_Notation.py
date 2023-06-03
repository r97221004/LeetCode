# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack[-1]
