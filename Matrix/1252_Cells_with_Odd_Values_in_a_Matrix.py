# 時間複雜度 O(n + m + L),  L 是 indices 的長度
# 空間複雜度 O(n + m)
class Solution:
    def oddCells(self, m, n, indices):
        row = [0]*m
        col = [0]*n

        for i, j in indices:
            row[i] ^= 1
            col[j] ^= 1
        
        R, C = sum(row), sum(col)
        return R*n + C*m - 2*R*C 

p = Solution()
print(p.oddCells(2, 3, indices = [[0,1], [1,1]]))


# 時間複雜度 O(n + m + L)
# 空間複雜度 O(n + m)
class Solution:
    def oddCells(self, m, n, indices):
        row = {}
        col = {}
        
        for i, j in indices:
            row[i] = row.get(i, 0) + 1
            col[j] = col.get(j, 0 ) + 1
            
        row = sum(i%2 for i in row.values())
        col = sum(i%2 for i in col.values())
           
        return row*n + col*m - 2*row*col

p = Solution()
print(p.oddCells(2, 3, indices = [[0,1], [1,1]]))


