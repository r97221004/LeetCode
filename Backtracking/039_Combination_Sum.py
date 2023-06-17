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
        self.find(start, nums, target, total+nums[start], comb)
        comb.pop()
        self.find(start + 1, nums, target, total, comb)

    def combinationSum(self, candidates, target):
        self.find(0, candidates, target, 0, [])
        return self.ans


p = Solution()
print(p.combinationSum(candidates=[2, 3, 6, 7], target=7))
