# 時間複雜度: O(n)
# 空間複雜度: O(1), 英文字母最多 26 個
class Solution:
    def firstUniqChar(self, s):
        count = {}
        
        for i in s:
            count[i] = count.get(i, 0) + 1
        
        for i, val in enumerate(s):
            if count[val] == 1: return i
            
        return -1

p = Solution()
print(p.firstUniqChar("leetcode"))