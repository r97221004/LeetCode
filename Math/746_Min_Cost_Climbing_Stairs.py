# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
            
        return min(cost[-1], cost[-2])

p = Solution()
print(p.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))