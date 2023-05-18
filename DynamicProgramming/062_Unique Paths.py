# 時間複雜度: O(m*n)
# 空間複雜度: O(n)
class Solution:
    def uniquePaths(self, m, n):
        row = [1]*n

        for i in range(m - 2, -1, -1):
            nowRow = [1]*n
            for j in range(n - 2, -1, -1):
                nowRow[j] = nowRow[j + 1] + row[j]
            row = nowRow

        return row[0]


p = Solution()
print(p.uniquePaths(m=3, n=7))


# 時間複雜度: O(m*n)
# 空間複雜度: O(n)
class Solution:
    def uniquePaths(self, m, n):
        dp = [1]*(n)

        for _ in range(m-1):
            for j in range(1, n):
                dp[j] =dp[j-1] + dp[j]
                
        return dp[-1]


p = Solution()
print(p.uniquePaths(m=3, n=7))