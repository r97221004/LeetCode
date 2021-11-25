# 時間複雜度: O(n^3)
# 空間複雜度: O(n)
class Solution:
    def longestPalindrome(self, s):
        logest = 0
        res = ''
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    if len(s[i:j + 1]) > logest:
                        res, logest = s[i:j + 1], len(s[i:j + 1])
                        
                        
        return res

p = Solution()
print(p.longestPalindrome("babad"))


# 時間複雜度: O(n^2)
# 空間複雜度: O(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)
             # odd case, like "aba"  # even case, like "abba"
        return res
        
         
    def helper(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


p = Solution()
print(p.longestPalindrome("babad"))