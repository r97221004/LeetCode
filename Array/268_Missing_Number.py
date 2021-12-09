# Bit Manipulation
# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def missingNumber(self, nums):
        res = len(nums)
        for i, val in enumerate(nums):
            res ^= i^val
        
        return res

p = Solution()
print(p.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))


# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def missingNumber(self, nums):
        data = {}
        for i in nums:
            data[i] = 1
        
        for i in range(0, len(nums) + 1):
            if i not in data:
                return i

p = Solution()
print(p.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))