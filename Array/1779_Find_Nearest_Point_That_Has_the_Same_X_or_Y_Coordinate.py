# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def nearestValidPoint(self, x, y, points):
        res = -1
        minDis = float('inf')
        
        for idx, (i, j) in enumerate(points):
            if (i == x or j == y) and (abs(i - x) + abs(j - y) < minDis):
                res = idx
                minDis = abs(i - x) + abs(j - y)
                
        return res

p = Solution()
print(p.nearestValidPoint(x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))