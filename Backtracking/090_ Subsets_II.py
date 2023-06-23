class Solution:
    def __init__(self):
        self.ans = []

    def find(self, start, nums, subset):
        if start >= len(nums):
            self.ans.append(subset[:])
            return

        subset.append(nums[start])
        self.find(start + 1, nums, subset)
        subset.pop()

        while start + 1 < len(nums) and nums[start] == nums[start + 1]:
            start += 1
        self.find(start + 1, nums, subset)

    def subsetsWithDup(self, nums):
        nums.sort()
        self.find(0, nums, [])
        return self.ans


p = Solution()
print(p.subsetsWithDup(nums=[1, 2, 2]))
