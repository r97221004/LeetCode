# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def maxProduct(self, nums):
        maxProd = nums[0]
        curMin = 1
        curMax = 1

        for n in nums:
            curMax, curMin = max(curMin*n, curMax*n,
                                 n), min(curMin*n, curMax*n, n)
            maxProd = max(maxProd, curMax)

        return maxProd


p = Solution()
print(p.maxProduct([2, 3, -2, 4]))
