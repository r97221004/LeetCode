# 時間複雜度: O(n)
# 空間複雜度: O(1)
# Fibonacci Number
class Solution:
    def fib(self, n):
        a, b = 0, 1
        
        for _ in range(0, n):
            a, b = b, a + b
        
        return a
        
p = Solution()
print(p.fib(4))