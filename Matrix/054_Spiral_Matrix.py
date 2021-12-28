# 時間複雜度: ?
# 空間複雜度: O(1)
class Solution:
    def spiralOrder(self, matrix):
        res = []

        while matrix:
            res.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]

        return res

p = Solution()
print(p.spiralOrder( [[1,2,3], [4,5,6], [7,8,9]]))



