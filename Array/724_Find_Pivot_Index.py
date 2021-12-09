# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        for i, val in enumerate(nums):
            if left == total - nums[i] - left:
                return i
            left += nums[i]
            
        return -1

p = Solution()
print(p.pivotIndex([1, 7, 3, 6, 5, 6]))