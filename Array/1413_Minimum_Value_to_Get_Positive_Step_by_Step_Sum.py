# 時間複雜度: O(n)
# 空間複雜度: O(1)

class Solution:
    def minStartValue(self, nums):
        prefixSum = 0
        minStart = 1
        
        for num in nums:
            prefixSum += num
            minStart = max(minStart, 1 - prefixSum)
            
        return minStart

p = Solution()
print(p.minStartValue([-3,2,-3,4,2]))