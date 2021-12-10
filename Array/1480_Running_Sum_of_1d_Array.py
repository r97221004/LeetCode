# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def runningSum(self, nums):
        prefix_sum = 0
        
        for i, val in enumerate(nums):
            prefix_sum += val
            nums[i] = prefix_sum
        
        return nums

p = Solution()
print(p.runningSum([1, 2, 3, 4]))