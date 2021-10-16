# Kadane's algorithm
# 時間複雜度: O(n)
# 如果不想用 max() 函式，可以再寫一個迴圈
class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


p = Solution()
print(p.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

