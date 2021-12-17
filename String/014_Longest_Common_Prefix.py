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
print(p.longestCommonPrefix(["flower", "flow", "flight"]))

# 時間複雜度: O(m*n), m 是 strs 裡面最小字串的長度, n 是 strs 的長度
# 空間複雜度: O(1)
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        
        count = float("inf")
        for a, b in zip(strs, strs[1:]):
            count = min(self.helper(a, b), count)
            if count == 0: return ""
            
        return strs[0][:count]
        
    def helper(self, a, b):
        count = 0
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                count += 1
            else:
                break
                
        return count

p = Solution()
print(p.longestCommonPrefix(["flower", "flow", "flight"]))