# 時間複雜度: O(n*m), n = len(grid), m = len(grid[0])
# 空間複雜度: O(n*m)
import collections


class Solution:
    def numIslands(self, grid):
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

            if i - 1 >= 0:
                self.dfs(grid, i - 1, j)
            if i + 1 <= len(grid) - 1:
                self.dfs(grid, i + 1, j)
            if j - 1 >= 0:
                self.dfs(grid, i, j - 1)
            if j + 1 <= len(grid[0]) - 1:
                self.dfs(grid, i, j + 1)


p = Solution()
print(p.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and
                            (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands


p = Solution()
print(p.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
