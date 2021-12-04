# 時間複雜度: ?
# 空間複雜度: ? 
class Solution:
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans
    
    def dfs(self, left, right, ans, String):
        if right < left:
            return
        if not right and not left:
            ans.append(String)
            return       
        if left:
            self.dfs(left - 1, right, ans, String + "(")
        if right:
            self.dfs(left, right - 1, ans, String + ')' )

p = Solution()
print(p.generateParenthesis( n = 3))