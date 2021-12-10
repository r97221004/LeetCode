# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCdy = max(candies)
        
        for i, val in enumerate(candies):
            if val + extraCandies >= maxCdy:
                candies[i] = True
            else:
                candies[i] = False
                
        return candies

p = Solution()
print(p.kidsWithCandies([2, 3, 5, 1, 3], 3))