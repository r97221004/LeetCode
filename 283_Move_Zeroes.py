# 時間複雜度: O(n)
class Solution:
    def moveZeroes(self, nums):
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
        for i in range(len(nums)):
            if i >= start:
                nums[i] = 0
        return nums
p = Solution()
print(p.moveZeroes([0,1,0,3,12]))
