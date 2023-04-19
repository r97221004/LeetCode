# Kadane's algorithm
# 時間複雜度: O(nlogn)
# 空間複雜度: O(1)
class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


p = Solution()
print(p.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0

            curSum += n
            maxSum = max(maxSub, curSum)

        return maxSum


p = Solution()
print(p.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
