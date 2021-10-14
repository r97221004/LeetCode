# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def sumZero(self, n):
        a = list(range(1, n))
        return a + [ -(n - 1)*n/2 ]