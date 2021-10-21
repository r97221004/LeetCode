# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def nearestValidPoint(self, x, y, points):
        mindis = float('inf')
        idx = -1
        
        for k, [i, j] in enumerate(points):
            if i == x or j == y:
                if abs(i - x) + abs(j - y) < mindis:
                    mindis = abs(i - x) + abs(j - y)
                    idx = k
        
        return idx

p = Solution()
print(p.nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]))