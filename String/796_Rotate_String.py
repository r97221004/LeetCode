# 時間複雜度: O(n^2), n = len(goal)
# 空間複雜度: O(1)
class Solution:
    def rotateString(self, s, goal):
        return len(s) == len(goal) and s in goal + goal

p = Solution()
print(p.rotateString("abcde", "cdeab"))