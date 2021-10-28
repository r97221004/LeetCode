# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def reverseString(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            
        return s

p = Solution()
print(p.reverseString(["h","e","l","l","o"]))
    