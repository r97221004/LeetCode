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
        row = len(grid) - 1
        col = 0
        res = 0
        
        while row >= 0 and col < len(grid[0]):
            if grid[row][col] < 0:
                res += len(grid[0]) - col
                row -= 1
            else:
                col += 1
            
        return res

p = Solution()
print(p.countNegatives([[4,3,2,-1], [3,2,1,-1], [1,1,-1,-2], [-1,-1,-2,-3]]))