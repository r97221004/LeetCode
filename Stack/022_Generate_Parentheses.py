# 時間複雜度: ?
# 空間複雜度: ?
class Solution:
    def generateParenthesis(self, n):
        left = n
        right = n
        res = []

        self.dfs(left, right, res, "")

        return res

    # 注意下面的 if 順序不能隨便對調
    def dfs(self, left, right, res, string):
        if right < left:
            return
        if not right and not left:
            res.append(string)
            return
        if left:
            self.dfs(left - 1, right, res, string + "(")
        if right:
            self.dfs(left, right - 1, res, string + ')')


p = Solution()
print(p.generateParenthesis(n=3))


class Solution:
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
            if openN > closeN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


p = Solution()
print(p.generateParenthesis(n=3))
