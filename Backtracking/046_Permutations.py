# Use `visited` set to record number which has been visited before.
class Solution:
    def __init__(self):
        self.ans = []

    def find(self, visited, nums, max_length, perm):
        if len(perm) == max_length:
            self.ans.append(perm[:])
            return
        for n in nums:
            if n not in visited:
                perm.append(n)
                visited.add(n)
                self.find(visited, nums, max_length, perm)
                perm.pop()
                visited.remove(n)

    def permute(self, nums):
        self.find(set(), nums, len(nums), [])
        return self.ans


s = Solution()
nums = [1, 2, 3]
print(s.permute(nums))
