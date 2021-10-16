# Kadane's algorithm
# 時間複雜度: O(n)
# 如果不想用 max() 函式，可以再寫一個迴圈
class Solution:
    def maxProfit(self, prices):
        for i in range(1, len(prices)):
            prices[i - 1] = prices[i] - prices[i - 1]
        prices[len(prices) - 1] = 0
        
        for i in range(1, len(prices)):
            if prices[i - 1] > 0:
                prices[i] += prices[i - 1]
                
        return max(prices)
p = Solution()
print(p.maxProfit([7,1,5,3,6,4]))