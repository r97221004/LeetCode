# 時間複雜度: O((n - m + 1)*m) - > O(n*m), n 是 haystack 的長度, m 是 needle 的長度   
# 空間複雜度: O(1)
class Solution:
    def strStr(self, haystack: str, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

p = Solution()
print(p.strStr("hello", "ll"))