# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def moveZeroes(self, nums):
        start = 0
        
        for i, val in enumerate(nums):
            if val != 0:
                nums[start] = val
                start += 1
        
        for i in range(start, len(nums)): nums[i] = 0

p = Solution()
print(p.moveZeroes([0, 1, 0, 3, 12]))
