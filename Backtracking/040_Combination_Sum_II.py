class Solution:
    def __init__(self):
        self.ans = []

    def find(self, start, nums, target, total, comb):
        if total == target:
            self.ans.append(comb[:])
            return
        if total > target:
            return
        if start >= len(nums):
            return

        comb.append(nums[start])
        self.find(start + 1, nums, target, total + nums[start], comb)
        comb.pop()

        while start + 1 < len(nums) and nums[start] == nums[start + 1]:
            start += 1

        self.find(start + 1, nums, target, total, comb)

    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.find(0, candidates, target, 0, [])
        return self.ans


p = Solution()
print(p.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
