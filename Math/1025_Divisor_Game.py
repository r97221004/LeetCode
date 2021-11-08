# 時間複雜度: O(1)
# 空間複雜度: O(1)
class Solution:
    def divisorGame(self, n):
        return n % 2 == 0
        
p = Solution()
print(p.divisorGame(3))