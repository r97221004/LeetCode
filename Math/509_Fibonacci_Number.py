# 時間複雜度: O(n)
# 空間複雜度: O(1)
# Fibonacci Number
class Solution:
    def fib(self, n):
        a, b = 0, 1
        
        for _ in range(n):
            a, b = b, a + b
        
        return a
        
p = Solution()
print(p.fib(4))


# 時間複雜度: O(2**n)
# 空間複雜度: O(n)
class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)
        
p = Solution()
print(p.fib(4))