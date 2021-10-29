# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def isSubsequence(self, s, t):
        start = 0
        for i, val in enumerate(t):
            if start <= len(s) - 1 and val == s[start]:
                start += 1
                
        return start == len(s)

p = Solution()
print(p.isSubsequence("abc", "ahbgdc"))