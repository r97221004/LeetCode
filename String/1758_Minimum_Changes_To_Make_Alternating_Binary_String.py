# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def minOperations(self, s):
        even = 0
        for i, val in enumerate(s):
            if int(val) != i%2: even += 1            
            
        return min(even, len(s) - even)
    
p = Solution()
print(p.minOperations("0100"))    