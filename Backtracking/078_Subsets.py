class Solution:
    def __init__(self):
        self.ans = []

    def find(self, start, nums, subset):
        self.ans.append(subset[:])
        if start >= len(nums):
            return

        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.find(i + 1, nums, subset)
            subset.pop()

    def subsets(self, nums):
        self.find(0, nums, [])
        return self.ans


p = Solution()
print(p.subsets(nums=[1, 2, 3]))


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
        self.find(start + 1, nums, subset)

    def subsets(self, nums):
        self.find(0, nums, [])
        return self.ans


p = Solution()
print(p.subsets(nums=[1, 2, 3]))