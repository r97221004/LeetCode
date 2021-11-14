# 時間複雜度: O(n*m), n = len(grid), m = len(grid[0])
# 空間複雜度: O(n*m)
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
                    
        return count
                    
    
    def dfs(self, grid, i, j):
        if grid[i][j] == "1":
            grid[i][j] = "#"
        
            if i - 1 >= 0: self.dfs(grid, i - 1, j)
            if i + 1 <= len(grid) - 1: self.dfs(grid, i + 1, j)
            if j - 1 >= 0: self.dfs(grid, i, j - 1)
            if j + 1 <= len(grid[0]) - 1: self.dfs(grid, i, j + 1)

p = Solution()
print(p.numIslands( grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))