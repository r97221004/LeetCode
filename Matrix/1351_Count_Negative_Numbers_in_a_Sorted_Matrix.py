# This solution uses the fact that the negative regions of the matrix will form a "staircase" shape, e.g.:
# ++++++
# ++++--
# ++++--
# +++---
# +-----
# +-----

# 時間複雜度: O(m + n)
# 空間複雜度: O(1)
class Solution:
    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        r, c, cnt = m - 1, 0, 0
        while r >= 0 and c <= n - 1:
            if grid[r][c] < 0:
                cnt += n - c
                r -= 1
            else:
                c += 1
        
        return cnt

p = Solution()
print(p.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))