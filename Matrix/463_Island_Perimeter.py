# 時間複雜度: O(m*n)
# 空間複雜度: O(1)
class Solution:
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        result = 0 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    
                    if r - 1 >= 0 and grid[r - 1][c] == 1:
                        result -= 2
                    
                    if c - 1 >= 0 and grid[r][c - 1] == 1:
                        result -= 2
                    
        return result

p = Solution()
print(p.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))