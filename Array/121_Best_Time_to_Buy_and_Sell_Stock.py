# Kadane's algorithm
# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def maxProfit(self, prices):
        for i in range(1, len(prices)):
            prices[i - 1] = prices[i] - prices[i - 1]
        prices[-1] = 0
        
        for i in range(1, len(prices)):
            if prices[i - 1] > 0:
                prices[i] += prices[i - 1]
                
        return max(prices)
p = Solution()
print(p.maxProfit([7, 1, 5, 3, 6, 4]))


class Solution:
    def maxProfit(self, prices):
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit >= 0:
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit


p = Solution()
print(p.maxProfit([7, 1, 5, 3, 6, 4]))

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        start = 0


        for index, p in enumerate(prices):
            diff = p - prices[start]
            max_profit = max(max_profit, diff)
            if diff < 0:
                start = index

        return max_profit


p = Solution()
print(p.maxProfit([7, 1, 5, 3, 6, 4]))