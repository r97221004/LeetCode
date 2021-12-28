# 時間複雜度: O(m*n)
# 空間複雜度: O(1)
class Solution:
    def islandPerimeter(self, grid):
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    res += 4
                    
                    if i - 1 >= 0 and grid[i - 1][j] == 1: res -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1: res -= 2
                                             
        return res
        
p = Solution()
print(p.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))