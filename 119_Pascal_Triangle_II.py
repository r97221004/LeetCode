# 時間複雜度: 2 + 3 + 4 ... + (n + 1) = [2 + (n + 1)]*(n)]/2 -> O(n**2)
class Solution:
    def getRow(self, rowIndex):
        row = [1]
        
        for _ in range(rowIndex):
            row = [i + j   for i, j in zip([0] + row, row + [0])]
        return row

p = Solution()
print(p.getRow(4))