# 時間複雜度 O(n + m + L),  L 是 indices 的長度
# 空間複雜度 O(n + m)
class Solution:
    def oddCells(self, n, m, indices):
        row = [0]*n
        col = [0]*m
        for i, j in indices:
            row[i] ^= 1
            col[j] ^= 1
        
        R, C = sum(row), sum(col)
        return R*m + C*n - 2*R*C 

p = Solution()
print(p.oddCells(2, 3, indices = [[0,1],[1,1]]))


