# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def isSubsequence(self, s, t):
        start = 0
        
        for i in t:
            if start < len(s) and i == s[start]:   # 注意兩個位置不能對調
                start += 1
                
        return start == len(s)

p = Solution()
print(p.isSubsequence("abc", "ahbgdc"))