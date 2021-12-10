# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def minStartValue(self, nums):
        ans = 1
        prefix = 0
        
        for i in nums:
            prefix += i
            if prefix < 1:
                ans = max(ans, 1 - prefix)
                
        return ans

p = Solution()
print(p.minStartValue([-3, 2, -3, 4, 2]))