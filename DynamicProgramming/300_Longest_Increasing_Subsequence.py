# 時間複雜度: O(n**2)
# 空間複雜度: O(n)
class Solution:
    def lengthOfLIS(self, nums):
        LIS = [1]*len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        return max(LIS)


p = Solution()
print(p.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
