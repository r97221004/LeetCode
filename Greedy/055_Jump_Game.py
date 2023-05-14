# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


p = Solution()
print(p.canJump(nums=[2, 3, 1, 1, 4]))
