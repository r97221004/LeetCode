# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def validPalindrome(self, s):
        start, end = 0, len(s) - 1
        
        while start < end:
            if s[start] != s[end]:
                a, b= s[start + 1:end + 1], s[start:end]
                return a == a[::-1] or b == b[::-1]
            
            start += 1
            end -= 1
        
        return True

p = Solution()
print(p.validPalindrome("aba"))