# Use `visited` set to record number which has been visited before.
class Solution:
    def __init__(self):
        self.ans = []

    def find(self, visited, nums, permutation):
        if (len(visited) == len(nums)):
            self.ans.append(permutation[:])
            return

        for n in nums:
            if n not in visited:
                visited.add(n)
                permutation.append(n)
                self.find(visited, nums, permutation)
                visited.remove(n)
                permutation.pop()

    def permute(self, nums):
        self.ans = []
        self.find(set(), nums, [])
        return self.ans


s = Solution()
nums = [1, 2, 3]
print(s.permute(nums))
