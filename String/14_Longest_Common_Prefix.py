# 時間複雜度: O(m*n), m 是 strs 裡面最小字串的長度, n 是 strs 的長度
# 空間複雜度: O(m), m 是 strs 裡面最小字串的長度
# 注意 len(String) 與 len(List) 的時間複雜度都是 O(1)
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

p = Solution()
print(p.longestCommonPrefix(["flower","flow","flight"]))

