# 時間複雜度: O(n)
# 空間複雜度：O(1)
class Solution:
    def rob(self, nums):
        # [rob1, rob2, n, n+1, ...]
        rob1, rob2 = 0, 0

        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)

        return rob2


p = Solution()
print(p.rob(nums=[1, 2, 3, 1]))
