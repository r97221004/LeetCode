# 時間複雜度: O(n*m)?
# 空間複雜度: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict):
        dp = [False]*(len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


p = Solution()
print(p.wordBreak(s="leetcode", wordDict=["leet", "code"]))
