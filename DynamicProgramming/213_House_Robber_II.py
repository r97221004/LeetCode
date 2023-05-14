# 時間複雜度：O(n)
# 空間複雜度：O(1)
class Solution:
    def rob(self, nums):
        return max(self.helper(nums[1:]), self.helper(nums[:-1]), nums[0])

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            rob1, rob2 = rob2, max(rob1 + n, rob2)

        return rob2


p = Solution()
print(p.rob(nums=[2, 3, 2]))
